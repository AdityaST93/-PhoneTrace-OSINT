import csv
import os
from datetime import datetime


def export_result(result):
    os.makedirs("data", exist_ok=True)

    filename = "data/phone_osint_report.csv"

    file_exists = os.path.isfile(filename)

    if "error" in result:
        print("Cannot export invalid result.")
        return

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=result.keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(result)

    print(f"\nReport saved: {filename}")