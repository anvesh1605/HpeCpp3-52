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
    output_dir: Path

    @property
    def run_name(self) -> str:
        return f"{self.switch}-{self.version}"


def discover_jobs(data_root: Path, output_root: Path) -> List[DatasetJob]:
    jobs: List[DatasetJob] = []
    for file_path in data_root.rglob("train_chat.jsonl"):
        if len(file_path.parts) < 3:
            continue
        version = file_path.parent.name
        switch = file_path.parent.parent.name
        output_dir = output_root / switch / version
        jobs.append(
            DatasetJob(
                switch=switch,
                version=version,
                data_path=file_path,
                output_dir=output_dir,
            )
        )
    jobs.sort(key=lambda job: (job.switch, job.version))
    return jobs


def filter_jobs(
    jobs: Sequence[DatasetJob],
    switches: Sequence[str],
    versions: Sequence[str],
    skip_existing: bool,
    limit: int,
) -> List[DatasetJob]:
    switch_set = {value.strip() for value in switches if value.strip()}
    version_set = {value.strip() for value in versions if value.strip()}
    filtered: List[DatasetJob] = []
    for job in jobs:
        if switch_set and job.switch not in switch_set:
            continue
        if version_set and job.version not in version_set:
            continue
        if skip_existing and (job.output_dir / "lora_adapters").exists():
            continue
        filtered.append(job)
        if limit > 0 and len(filtered) >= limit:
            break
    return filtered


def build_cmd(
    python_exe: str,
    model_name: str,
    template: str,
    job: DatasetJob,
    passthrough_args: Sequence[str],
) -> List[str]:
    cmd: List[str] = [
        python_exe,
        "train.py",
        "--data_path",
        str(job.data_path),
        "--model_name",
        model_name,
        "--template",
        template,
        "--output_dir",
        str(job.output_dir),
        "--run_name",
        job.run_name,
    ]
    cmd.extend(arg for arg in passthrough_args if arg != "--")
    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run sequential fine-tuning jobs for final_json/*/*/train_chat.jsonl"
    )
    parser.add_argument("--data_root", type=str, default="final_json")
    parser.add_argument("--output_root", type=str, default="outputs")
    parser.add_argument("--model_name", type=str, required=True)
    parser.add_argument("--template", type=str, default="llama3")
    parser.add_argument("--switches", nargs="*", default=[])
    parser.add_argument("--versions", nargs="*", default=[])
    parser.add_argument("--skip_existing", action="store_true")
    parser.add_argument("--stop_on_error", action="store_true")
    parser.add_argument("--dry_run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--python_exe", type=str, default=sys.executable)
    args, passthrough = parser.parse_known_args()

    data_root = Path(args.data_root)
    output_root = Path(args.output_root)
    if not data_root.exists():
        print(f"Data root does not exist: {data_root}")
        return 2

    jobs = discover_jobs(data_root, output_root)
    jobs = filter_jobs(
        jobs=jobs,
        switches=args.switches,
        versions=args.versions,
        skip_existing=args.skip_existing,
        limit=args.limit,
    )
    if not jobs:
        print("No jobs selected. Check filters or paths.")
        return 0

    print(f"Selected jobs: {len(jobs)}")
    print(f"Passthrough args to train.py: {passthrough}")

    failures = 0
    for idx, job in enumerate(jobs, start=1):
        cmd = build_cmd(
            python_exe=args.python_exe,
            model_name=args.model_name,
            template=args.template,
            job=job,
            passthrough_args=passthrough,
        )
        print(f"\n[{idx}/{len(jobs)}] {job.run_name}")
        print(" ".join(cmd))

        if args.dry_run:
            continue

        job.output_dir.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(cmd, check=False)
        if result.returncode != 0:
            failures += 1
            print(f"Job failed ({job.run_name}) with code {result.returncode}")
            if args.stop_on_error:
                print("Stopping due to --stop_on_error")
                return result.returncode

    if args.dry_run:
        print("\nDry run complete.")
        return 0

    if failures:
        print(f"\nCompleted with {failures} failed job(s).")
        return 1

    print("\nAll jobs completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
