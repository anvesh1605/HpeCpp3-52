import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence


@dataclass
class DatasetJob:
    switch: str
    version: str
    data_path: Path


def discover_jobs(data_root: Path) -> List[DatasetJob]:
    jobs: List[DatasetJob] = []
    for path in data_root.rglob("train_chat.jsonl"):
        if len(path.parts) < 3:
            continue
        jobs.append(
            DatasetJob(
                switch=path.parent.parent.name,
                version=path.parent.name,
                data_path=path,
            )
        )
    jobs.sort(key=lambda item: (item.switch, item.version))
    return jobs


def filter_jobs(
    jobs: Sequence[DatasetJob],
    switches: Sequence[str],
    versions: Sequence[str],
    limit: int,
) -> List[DatasetJob]:
    switch_set = {item.strip() for item in switches if item.strip()}
    version_set = {item.strip() for item in versions if item.strip()}
    selected: List[DatasetJob] = []
    for job in jobs:
        if switch_set and job.switch not in switch_set:
            continue
        if version_set and job.version not in version_set:
            continue
        selected.append(job)
        if limit > 0 and len(selected) >= limit:
            break
    return selected


def run_name(template: str, switch: str, version: str) -> str:
    return f"{template}-{switch}-{version}"


def train_cmd(
    python_exe: str,
    model_name: str,
    template: str,
    job: DatasetJob,
    output_dir: Path,
    init_adapter_path: Path | None,
    passthrough: Sequence[str],
) -> List[str]:
    cmd = [
        python_exe,
        "train.py",
        "--data_path",
        str(job.data_path),
        "--model_name",
        model_name,
        "--template",
        template,
        "--output_dir",
        str(output_dir),
        "--run_name",
        run_name(template, job.switch, job.version),
    ]
    if init_adapter_path is not None:
        cmd.extend(["--init_adapter_path", str(init_adapter_path)])
    cmd.extend(arg for arg in passthrough if arg != "--")
    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run fine-tuning over final_json datasets one by one for multiple templates. "
            "Supports optional incremental adapter chaining per template."
        )
    )
    parser.add_argument("--data_root", type=str, default="final_json")
    parser.add_argument("--output_root", type=str, default="outputs_templates")
    parser.add_argument("--model_name", type=str, required=True)
    parser.add_argument("--templates", nargs="+", required=True)
    parser.add_argument("--switches", nargs="*", default=[])
    parser.add_argument("--versions", nargs="*", default=[])
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--incremental", action="store_true")
    parser.add_argument("--skip_existing", action="store_true")
    parser.add_argument("--stop_on_error", action="store_true")
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--python_exe", type=str, default=sys.executable)
    args, passthrough = parser.parse_known_args()

    data_root = Path(args.data_root)
    output_root = Path(args.output_root)
    if not data_root.exists():
        print(f"Data root does not exist: {data_root}")
        return 2

    jobs = filter_jobs(
        jobs=discover_jobs(data_root),
        switches=args.switches,
        versions=args.versions,
        limit=args.limit,
    )
    if not jobs:
        print("No datasets selected.")
        return 0

    print(f"Templates: {args.templates}")
    print(f"Datasets selected: {len(jobs)}")
    print(f"Passthrough args to train.py: {passthrough}")

    failures = 0
    total = len(args.templates) * len(jobs)
    progress = 0

    for template in args.templates:
        prev_adapter: Path | None = None
        print(f"\n=== TEMPLATE: {template} ===")
        for job in jobs:
            progress += 1
            output_dir = output_root / template / job.switch / job.version
            adapter_dir = output_dir / "lora_adapters"

            if args.skip_existing and adapter_dir.exists():
                print(f"[{progress}/{total}] skip existing {template} {job.switch}/{job.version}")
                if args.incremental:
                    prev_adapter = adapter_dir
                continue

            init_adapter = prev_adapter if args.incremental else None
            cmd = train_cmd(
                python_exe=args.python_exe,
                model_name=args.model_name,
                template=template,
                job=job,
                output_dir=output_dir,
                init_adapter_path=init_adapter,
                passthrough=passthrough,
            )

            print(f"[{progress}/{total}] {template} | {job.switch}/{job.version}")
            print(" ".join(cmd))
            if args.dry_run:
                if args.incremental:
                    # In dry-run mode we still move the chain logically to expected output path.
                    prev_adapter = adapter_dir
                continue

            output_dir.mkdir(parents=True, exist_ok=True)
            rc = subprocess.run(cmd, check=False).returncode
            if rc != 0:
                failures += 1
                print(f"FAILED ({rc}): {template} | {job.switch}/{job.version}")
                if args.stop_on_error:
                    return rc
            else:
                if args.incremental:
                    prev_adapter = adapter_dir

    if args.dry_run:
        print("\nDry run complete.")
        return 0

    if failures:
        print(f"\nCompleted with {failures} failed runs.")
        return 1

    print("\nAll runs completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
