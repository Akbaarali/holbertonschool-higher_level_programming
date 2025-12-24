#!/usr/bin/env python3
"""Convert CSV to JSON."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert csv_filename to JSON and write to data.json.
    Return True on success, False on failure.
    """
    try:
        with open(csv_filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return True
    except Exception:
        return False
