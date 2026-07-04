from __future__ import annotations

from pathlib import Path

from markitdown import MarkItDown


SOURCE_ROOT = Path(__file__).resolve().parent
OUTPUT_ROOT = SOURCE_ROOT / "markitdown_source_output"


def source_roots() -> list[Path]:
    return sorted(
        path
        for path in SOURCE_ROOT.iterdir()
        if path.is_dir() and path.name.lower().startswith("aruba_")
    )


def target_path_for(source_file: Path) -> Path:
    relative = source_file.relative_to(SOURCE_ROOT)
    if source_file.suffix:
        relative = relative.with_suffix(".md")
    else:
        relative = relative.with_name(f"{relative.name}.md")
    return OUTPUT_ROOT / relative


def mirror_directories(roots: list[Path]) -> int:
    count = 0
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    for root in roots:
        for directory in [root, *[p for p in root.rglob("*") if p.is_dir()]]:
            (OUTPUT_ROOT / directory.relative_to(SOURCE_ROOT)).mkdir(parents=True, exist_ok=True)
            count += 1
    return count


def main() -> None:
    roots = source_roots()
    directories_mirrored = mirror_directories(roots)
    files = sorted(file for root in roots for file in root.rglob("*") if file.is_file())

    converter = MarkItDown(enable_plugins=False)
    converted = 0
    skipped = 0
    failed: list[str] = []

    for source_file in files:
        target_file = target_path_for(source_file)
        if target_file.exists():
            skipped += 1
            continue

        try:
            result = converter.convert(str(source_file))
            markdown = result.text_content or result.markdown or ""
            target_file.parent.mkdir(parents=True, exist_ok=True)
            target_file.write_text(markdown.rstrip() + "\n", encoding="utf-8")
            converted += 1
            if converted % 500 == 0:
                print(f"Converted {converted} files, skipped {skipped} existing...")
        except Exception as exc:  # noqa: BLE001 - continue the batch and report all misses.
            failed.append(f"{source_file}: {exc}")

    print(f"Source root: {SOURCE_ROOT}")
    print(f"Output root: {OUTPUT_ROOT}")
    print(f"Source folders: {len(roots)}")
    print(f"Directories mirrored: {directories_mirrored}")
    print(f"Source files found: {len(files)}")
    print(f"Files converted: {converted}")
    print(f"Files skipped: {skipped}")
    print(f"Failures: {len(failed)}")
    for item in failed[:100]:
        print(f"FAILED: {item}")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
