import os
import time
import json
import re
from urllib.parse import urlparse, parse_qs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# CONFIGURATION - MODIFY THESE SETTINGS
SWITCH = "10000"
SWITCH_DIR_NAME = SWITCH.replace("/", "_")

# Map of VERSION -> SUB_VERSIONS
VERSIONS_CONFIG = {
    "10_18": ["0001"],
}
PORTAL_URL = "https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007259en_us&docLocale=en_US"

DOCDISPLAY_HOST_FRAGMENT = "support.hpe.com/hpesc/public/docDisplay"
CANONICAL_SECTION_FILE_MAP = {
    "overview": "overview",
    "enhancements": "enhancements",
    "resolved issues": "fixes",
    "feature caveats": "caveats",
    "known issues": "issues",
}
IGNORE_LINK_TEXTS = {
    "table of contents",
    "feedback",
    "privacy",
    "terms of use",
    "ad choices & cookies",
}
VERSION_SERIES_RE = re.compile(r"^aos-cx\s+\d+\.\d+\.xx$", re.IGNORECASE)
VERSION_POINT_RE = re.compile(r"^\d+\.\d+\.\d{4}$")

BASE_HTML_CONTENT_PATH = os.path.abspath(f"Aruba_{SWITCH_DIR_NAME}_HTML_Content")
JSON_CONTENT_PATH = os.path.abspath(f"Aruba_{SWITCH_DIR_NAME}_JSON_Content")


def ensure_output_directories():
    os.makedirs(BASE_HTML_CONTENT_PATH, exist_ok=True)
    os.makedirs(JSON_CONTENT_PATH, exist_ok=True)

    for version, subversions in VERSIONS_CONFIG.items():
        version_dir = os.path.join(BASE_HTML_CONTENT_PATH, version)
        os.makedirs(version_dir, exist_ok=True)
        for subversion in subversions:
            os.makedirs(os.path.join(version_dir, subversion), exist_ok=True)


def wait_for(driver, condition, timeout=12):
    return WebDriverWait(driver, timeout).until(condition)


def switch_to_release_notes_frame(driver, timeout=15):
    driver.switch_to.default_content()
    iframes = driver.find_elements(By.CSS_SELECTOR, "iframe#releaseNotes")
    if not iframes:
        return None
    iframe = iframes[0]
    driver.switch_to.frame(iframe)
    return iframe


def select_switch(driver, switch_name):
    """Select switch from outer-page dropdown that updates iframe src."""
    print(f"\nSelecting switch: {switch_name}")
    try:
        driver.switch_to.default_content()
        dropdown = wait_for(driver, EC.presence_of_element_located((By.CSS_SELECTOR, "select#platformsForRNs, select[name='platform'], select")), 12)
        select = Select(dropdown)

        target_option_text = None
        for opt in select.options:
            text = (opt.text or "").strip()
            if text.lower() == switch_name.lower():
                target_option_text = text
                break

        if target_option_text is None:
            for opt in select.options:
                text = (opt.text or "").strip()
                if switch_name.lower() in text.lower():
                    target_option_text = text
                    break

        if target_option_text is None:
            available = ", ".join((o.text or "").strip() for o in select.options if (o.text or "").strip() and (o.text or "").strip() != "------")
            print(f"Switch '{switch_name}' not found. Available: {available}")
            return False

        iframe_before = driver.find_element(By.CSS_SELECTOR, "iframe#releaseNotes, iframe").get_attribute("src")
        select.select_by_visible_text(target_option_text)

        # Wait for iframe src to change to selected doc
        def src_changed(_):
            try:
                src_now = driver.find_element(By.CSS_SELECTOR, "iframe#releaseNotes, iframe").get_attribute("src")
                return src_now and src_now != iframe_before
            except Exception:
                return False

        WebDriverWait(driver, 20).until(src_changed)
        time.sleep(2)
        print(f"Switch '{target_option_text}' selected")
        return True
    except Exception as e:
        print(f"Error selecting switch: {e}")
        return False


def _get_visible_anchor_by_text(driver, text, timeout=10, exact=True):
    if exact:
        xpath = f"//a[normalize-space(.)='{text}']"
    else:
        xpath = f"//a[contains(normalize-space(.), '{text}')]"

    try:
        wait_for(driver, EC.presence_of_all_elements_located((By.XPATH, xpath)), timeout)
    except Exception:
        return None

    candidates = driver.find_elements(By.XPATH, xpath)
    for a in candidates:
        try:
            if a.is_displayed() and a.is_enabled():
                return a
        except Exception:
            continue

    return candidates[0] if candidates else None


def _click_link_by_text(driver, text, timeout=10):
    # First try exact match; if not found, try contains match.
    link = _get_visible_anchor_by_text(driver, text, timeout=timeout, exact=True)
    if not link:
        link = _get_visible_anchor_by_text(driver, text, timeout=timeout, exact=False)
    if not link:
        raise RuntimeError(f"Link not found for text: {text}")

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
    try:
        driver.execute_script("arguments[0].click();", link)
    except Exception:
        link.click()
    time.sleep(1)


def _wait_main_contains(driver, must_include, timeout=15):
    token = must_include.lower()

    def cond(_):
        try:
            main = driver.find_element(By.TAG_NAME, "main")
            return token in (main.text or "").lower()
        except Exception:
            return False

    WebDriverWait(driver, timeout).until(cond)


def _open_version(driver, version):
    version_text = f"{version.replace('_', '.')}.xx"
    _click_link_by_text(driver, version_text, timeout=12)
    _wait_main_contains(driver, version_text, timeout=15)


def _open_subversion(driver, version, subversion):
    sub_text = f"{version.replace('_', '.')}.{subversion}"
    _click_link_by_text(driver, sub_text, timeout=10)
    _wait_main_contains(driver, sub_text, timeout=15)


def _find_section_link_in_main(driver, candidate_texts):
    main = driver.find_element(By.TAG_NAME, "main")
    anchors = main.find_elements(By.TAG_NAME, "a")

    normalized = {t.lower(): t for t in candidate_texts}
    for a in anchors:
        text = (a.text or "").strip()
        if text.lower() in normalized:
            return a

    # relaxed contains fallback
    for a in anchors:
        text = (a.text or "").strip().lower()
        if any(c.lower() in text for c in candidate_texts):
            return a

    return None


def _save_current_page(driver, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(driver.page_source)


def _extract_page_key_from_href(href):
    try:
        parsed = urlparse(href)
        query = parse_qs(parsed.query)
        page = query.get("page", [None])[0]
        if not page:
            return None
        return page.strip()
    except Exception:
        return None


def _normalize_label(text):
    return re.sub(r"\s+", " ", (text or "").strip()).lower()


def _slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "_", (text or "").lower())
    slug = slug.strip("_")
    return slug or "section"


def _is_release_doc_link(href):
    href_l = (href or "").lower()
    return DOCDISPLAY_HOST_FRAGMENT.lower() in href_l and "page=" in href_l


def _collect_release_links_from_main(driver):
    """Collect candidate section/subsection links from the current main content."""
    main = driver.find_element(By.TAG_NAME, "main")
    anchors = main.find_elements(By.XPATH, ".//a[@href]")

    links = []
    seen = set()

    for anchor in anchors:
        text = re.sub(r"\s+", " ", (anchor.text or "").strip())
        href = (anchor.get_attribute("href") or "").strip()

        if not text or not href:
            continue
        if not _is_release_doc_link(href):
            continue

        label = _normalize_label(text)
        if label in IGNORE_LINK_TEXTS:
            continue
        if VERSION_SERIES_RE.match(text) or VERSION_POINT_RE.match(text):
            continue

        page_key = _extract_page_key_from_href(href)
        if not page_key:
            continue

        dedupe_key = (page_key, label)
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)

        links.append({"text": text, "href": href, "page_key": page_key})

    return links


def _open_release_link(driver, href, label):
    """Open a release link in the iframe context and wait for content to load."""
    main_before = ""
    try:
        main_before = driver.find_element(By.TAG_NAME, "main").text
    except Exception:
        pass

    clicked = False
    try:
        main = driver.find_element(By.TAG_NAME, "main")
        candidates = main.find_elements(By.XPATH, f".//a[@href='{href}']")
        for elem in candidates:
            if elem.is_displayed() and elem.is_enabled():
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
                try:
                    driver.execute_script("arguments[0].click();", elem)
                except Exception:
                    elem.click()
                clicked = True
                break
    except Exception:
        pass

    if not clicked:
        driver.execute_script("window.location.assign(arguments[0]);", href)

    label_lower = _normalize_label(label)

    def page_loaded(_):
        try:
            main_now = driver.find_element(By.TAG_NAME, "main").text
            if not main_now:
                return False
            if main_now != main_before:
                return True
            if label_lower and label_lower in main_now.lower():
                return True
            return False
        except Exception:
            return False

    WebDriverWait(driver, 15).until(page_loaded)
    time.sleep(0.8)


def _filename_for_section(label, page_key, used_filenames):
    normalized = _normalize_label(label)
    base = CANONICAL_SECTION_FILE_MAP.get(normalized) or _slugify(label)

    # Prevent collisions when the same label appears more than once.
    candidate = base
    if candidate in used_filenames:
        page_slug = _slugify(page_key.replace(".html", ""))
        candidate = f"{base}_{page_slug[:12]}"

    used_filenames.add(candidate)
    return f"{candidate}.html"


def save_release_section_pages(driver, version, subversion, subversion_dir):
    """
    Save every release section/subsection page linked from main content.
    This covers the full sidebar structure (including nested entries).
    """
    queue = _collect_release_links_from_main(driver)
    if not queue:
        print("    No section links found in current page")
        return 0

    visited_page_keys = set()
    queued_page_keys = {item["page_key"] for item in queue}
    used_filenames = set()
    index_records = []
    saved = 0

    while queue:
        item = queue.pop(0)
        page_key = item["page_key"]
        if page_key in visited_page_keys:
            continue

        try:
            _open_release_link(driver, item["href"], item["text"])
        except Exception as e:
            print(f"    Failed to open section '{item['text']}': {e}")
            visited_page_keys.add(page_key)
            continue

        filename = _filename_for_section(item["text"], page_key, used_filenames)
        output_path = os.path.join(subversion_dir, filename)
        _save_current_page(driver, output_path)
        saved += 1
        visited_page_keys.add(page_key)
        print(f"    Saved {filename}")

        index_records.append(
            {
                "label": item["text"],
                "filename": filename,
                "href": item["href"],
                "page_key": page_key,
            }
        )

        # Discover nested subtopics from the newly opened section page.
        for child in _collect_release_links_from_main(driver):
            child_key = child["page_key"]
            if child_key in visited_page_keys or child_key in queued_page_keys:
                continue
            queue.append(child)
            queued_page_keys.add(child_key)

    index_path = os.path.join(subversion_dir, "_sections_index.json")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "switch": SWITCH,
                "version": version,
                "subversion": subversion,
                "sections": index_records,
            },
            f,
            indent=2,
            ensure_ascii=False,
        )

    return saved


def scrape_portal_content(driver):
    print("\n" + "=" * 60)
    print("SCRAPING PORTAL CONTENT")
    print("=" * 60)

    total_items = sum(len(v) for v in VERSIONS_CONFIG.values())
    print(f"Switch: {SWITCH}")
    print(f"Total versions: {len(VERSIONS_CONFIG)}")
    print(f"Total subversions: {total_items}\n")

    switch_to_release_notes_frame(driver)

    item_count = 0
    for version, subversions in VERSIONS_CONFIG.items():
        print(f"\nVersion: {version}")
        try:
            _open_version(driver, version)
        except Exception as e:
            print(f"  Could not open version {version}: {e}")
            item_count += len(subversions)
            continue

        for subversion in subversions:
            item_count += 1
            display = f"{version}/{subversion}"
            subversion_dir = os.path.join(BASE_HTML_CONTENT_PATH, version, subversion)

            sections_index_file = os.path.join(subversion_dir, "_sections_index.json")
            if os.path.exists(sections_index_file) and os.path.getsize(sections_index_file) > 20:
                print(f"  [{item_count}/{total_items}] Skipping (already saved): {display}")
                continue

            print(f"  [{item_count}/{total_items}] Scraping: {display}")
            try:
                _open_subversion(driver, version, subversion)
                saved_count = save_release_section_pages(driver, version, subversion, subversion_dir)
                if saved_count == 0:
                    print("    No section pages saved for this release")

                # Go back to version page for next subversion
                _open_version(driver, version)
            except Exception as e:
                print(f"    Error scraping {display}: {e}")
                try:
                    _open_version(driver, version)
                except Exception:
                    pass

    print("\nALL CONTENT SCRAPED")


def _extract_table(table):
    rows = table.find_all("tr")
    if len(rows) < 2:
        return None

    headers = [cell.get_text(" ", strip=True) for cell in rows[0].find_all(["th", "td"])]
    if not headers:
        return None

    data_rows = []
    for row in rows[1:]:
        cells = [cell.get_text(" ", strip=True) for cell in row.find_all("td")]
        if cells and len(cells) == len(headers):
            data_rows.append({headers[i].lower(): cells[i] for i in range(len(headers))})

    if not data_rows:
        return None

    return {"type": "table", "headers": headers, "rows": data_rows}


def html_to_json():
    print("\n" + "=" * 60)
    print("CONVERTING HTML TO JSON")
    print("=" * 60 + "\n")

    for version in VERSIONS_CONFIG.keys():
        version_html_dir = os.path.join(BASE_HTML_CONTENT_PATH, version)
        if not os.path.exists(version_html_dir):
            continue

        for subversion in VERSIONS_CONFIG[version]:
            subversion_html_dir = os.path.join(version_html_dir, subversion)
            subversion_json_dir = os.path.join(JSON_CONTENT_PATH, version, subversion)
            os.makedirs(subversion_json_dir, exist_ok=True)

            if not os.path.exists(subversion_html_dir):
                continue

            html_files = [f for f in os.listdir(subversion_html_dir) if f.endswith(".html")]
            for html_file in html_files:
                html_path = os.path.join(subversion_html_dir, html_file)
                json_path = os.path.join(subversion_json_dir, html_file.replace(".html", ".json"))

                try:
                    with open(html_path, "r", encoding="utf-8") as f:
                        soup = BeautifulSoup(f.read(), "html.parser")

                    content_root = (
                        soup.find("main")
                        or soup.select_one("[role='main']")
                        or soup.find("body")
                    )

                    data = {
                        "version": version,
                        "subversion": subversion,
                        "page_name": html_file.replace(".html", ""),
                        "title": soup.title.string.strip() if soup.title and soup.title.string else "No Title",
                        "content": [],
                    }

                    if content_root:
                        for table in content_root.find_all("table"):
                            t = _extract_table(table)
                            if t:
                                data["content"].append(t)

                        current_section = None
                        for el in content_root.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol"]):
                            if el.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                                heading = el.get_text(" ", strip=True)
                                if heading:
                                    current_section = {"heading": heading, "level": el.name, "content": []}
                                    data["content"].append(current_section)
                                continue

                            if current_section is None:
                                current_section = {"heading": "Overview", "level": "h1", "content": []}
                                data["content"].append(current_section)

                            if el.name == "p":
                                txt = el.get_text(" ", strip=True)
                                if txt:
                                    current_section["content"].append(txt)
                            elif el.name in ["ul", "ol"]:
                                items = [li.get_text(" ", strip=True) for li in el.find_all("li") if li.get_text(" ", strip=True)]
                                if items:
                                    current_section["content"].append({"list": items})

                    with open(json_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)

                    print(f"  OK {version}/{subversion}/{os.path.basename(json_path)}")
                except Exception as e:
                    print(f"  Error converting {html_file}: {e}")

    print("\nALL HTML FILES CONVERTED TO JSON")


def main():
    ensure_output_directories()

    print("\n" + "=" * 60)
    print("ARUBA PORTAL SCRAPER")
    print("=" * 60)
    print(f"Switch: {SWITCH}")
    print(f"Portal URL: {PORTAL_URL}")
    print(f"\nVersions to scrape: {len(VERSIONS_CONFIG)}")
    for version, subversions in VERSIONS_CONFIG.items():
        print(f"  - {version}: {len(subversions)} subversions")
    print("=" * 60 + "\n")

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
    )

    try:
        print(f"Loading portal: {PORTAL_URL}\n")
        driver.get(PORTAL_URL)
        time.sleep(10)

        scrape_portal_content(driver)
        html_to_json()

        print("\n" + "=" * 60)
        print("ALL TASKS COMPLETED")
        print("=" * 60)
        print(f"\nHTML content saved to: {BASE_HTML_CONTENT_PATH}")
        print(f"JSON content saved to: {JSON_CONTENT_PATH}")

    except Exception as e:
        print(f"\nFatal error: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
