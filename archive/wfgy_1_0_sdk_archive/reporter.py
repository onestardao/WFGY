# wfgy_sdk/reporter.py

import os, json
from .utils import RESULTS_DIR

def generate_report(fmt, output):
    entries = []
    for fn in os.listdir(RESULTS_DIR):
        if fn.endswith(".json"):
            data = json.load(open(os.path.join(RESULTS_DIR, fn)))
            entries.append((fn.replace(".json",""), data))
    if fmt == "html":
        with open(output, "w") as f:
            f.write("<html><body><h1>Report</h1>")
            for name,data in entries:
                f.write(f"<h2>{name}</h2><pre>{data}</pre>")
            f.write("</body></html>")
    else:
        with open(output, "w") as f:
            for name,data in entries:
                f.write(f"## {name}\n{data}\n\n")
    print(f"Report saved to {output}")

