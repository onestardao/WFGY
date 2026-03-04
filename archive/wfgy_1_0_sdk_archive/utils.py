# wfgy_sdk/utils.py

import os
import hashlib

ROOT = os.path.abspath(os.path.dirname(__file__))
DATA_DIR    = os.path.join(ROOT, "..", "wfgy_data")
RESULTS_DIR = os.path.join(ROOT, "..", "wfgy_results")

def compute_checksum():
    base_path = os.path.dirname(__file__)
    checksum_map = {}
    print("Computing checksums for all .py files in wfgy_sdk...")

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                with open(full_path, "rb") as f:
                    content = f.read()
                    sha256 = hashlib.sha256(content).hexdigest()
                    rel_path = os.path.relpath(full_path, base_path)
                    checksum_map[rel_path] = sha256
                    print(f"{rel_path}: {sha256}")

    return checksum_map

