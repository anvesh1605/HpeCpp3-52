#!/usr/bin/env python3
"""
Run tests on all trained switch models and compile results
"""
import subprocess
import json
import os
from pathlib import Path

# Define test configurations - (switch, version, template)
TEST_CONFIGS = [
    ("4100i", "10_13", "tinyllama"),
    ("4100i", "10_14", "tinyllama"),
    ("4100i", "10_17", "tinyllama"),
    ("5420", "10_15", "tinyllama"),
    ("5420", "10_17", "tinyllama"),
    ("6000", "10_13", "tinyllama"),
    ("6000", "10_15", "tinyllama"),
    ("6000", "10_17", "tinyllama"),
    ("6100", "10_13", "tinyllama"),
    ("6100", "10_17", "tinyllama"),
    ("6200", "10_13", "tinyllama"),
    ("6200", "10_17", "tinyllama"),
    ("6300", "10_13", "tinyllama"),
    ("6300", "10_17", "tinyllama"),
    ("8100", "10_13", "tinyllama"),
    ("8100", "10_17", "tinyllama"),
    ("8320", "10_13", "tinyllama"),
    ("8320", "10_17", "tinyllama"),
]

BASE_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
SUB_VERSION = "0001"

def run_test(switch, version, template):
    """Run a single test configuration"""
    adapter_path = f"outputs_templates/{template}/{switch}/{version}/lora_adapters"
    
    # Check if adapter exists
    if not Path(adapter_path).exists():
        print(f"⚠ Skipping {switch}/{version} - adapter not found")
        return None
    
    output_file = f"test_results_{switch}_{version}_{template}.json"
    
    print(f"\n{'='*80}")
    print(f"Testing: {switch} | Firmware: {version} | Template: {template}")
    print(f"{'='*80}")
    
    cmd = [
        ".\.venv\Scripts\python.exe",
        "-u",
        "test_inference.py",
        "--base_model", BASE_MODEL,
        "--adapter_path", adapter_path,
        "--template", template,
        "--switch", switch,
        "--version", version,
        "--sub_version", SUB_VERSION,
        "--output_json", output_file,
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=False, timeout=1200)
        if result.returncode == 0:
            print(f"✓ Test completed for {switch}/{version}")
            return output_file
        else:
            print(f"✗ Test failed for {switch}/{version}")
            return None
    except subprocess.TimeoutExpired:
        print(f"✗ Test timed out for {switch}/{version}")
        return None
    except Exception as e:
        print(f"✗ Error testing {switch}/{version}: {e}")
        return None


def merge_results(result_files):
    """Merge all test results into one file"""
    all_results = []
    
    for result_file in result_files:
        if result_file and Path(result_file).exists():
            with open(result_file, "r") as f:
                data = json.load(f)
                if isinstance(data, list):
                    all_results.extend(data)
                else:
                    all_results.append(data)
    
    # Save merged results
    merged_file = "test_results_all_switches.json"
    with open(merged_file, "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n✓ Merged {len(all_results)} test results into {merged_file}")
    return merged_file


def main():
    print("Starting comprehensive tests on all trained switch models...\n")
    
    result_files = []
    
    for switch, version, template in TEST_CONFIGS:
        result_file = run_test(switch, version, template)
        if result_file:
            result_files.append(result_file)
    
    print(f"\n\nCompleted {len(result_files)} tests out of {len(TEST_CONFIGS)}")
    
    if result_files:
        merged_file = merge_results(result_files)
        print(f"\nAll results merged to: {merged_file}")
    else:
        print("No tests completed successfully")


if __name__ == "__main__":
    main()
