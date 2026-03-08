import os
from datetime import datetime

from scanner import scan_folder


PROJECT_FOLDER = "C:/Users/THINKPAD/Desktop/Python Refresher/Project Directory Auditor"   
REPORTS_FOLDER = os.path.join(PROJECT_FOLDER, "reports")


def make_reports_folder():
    if not os.path.exists(REPORTS_FOLDER):
        os.mkdir(REPORTS_FOLDER)


def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")   


def write_audit_report(files, timestamp):
    filename = f"audit_{timestamp}.txt"
    report_path = os.path.join(REPORTS_FOLDER, filename)

    with open(report_path, "w") as f:

        f.write("FILE AUDIT REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Folder: {PROJECT_FOLDER}\n")
        f.write(f"Total files: {len(files)}\n")
        f.write("=" * 50 + "\n\n")

        for file in files:
            modified_str = file["last_modified"].strftime("%Y-%m-%d %H:%M:%S")
            status = "STALE" if file["is_stale"] else "OK"

            f.write(f"Name: {file['name']}\n")
            f.write(f"Type: {file['type']}\n")
            f.write(f"Size: {file['size']} bytes\n")
            f.write(f"Modified: {modified_str}  ({file['days_old']} days ago)\n")
            f.write(f"Status: {status}\n")
            f.write("-" * 40 + "\n")

    return report_path

def write_penalties_report(files, timestamp):
    filename = f"penalties_{timestamp}.txt"
    report_path = os.path.join(REPORTS_FOLDER, filename)

    stale_files = [f for f in files if f["is_stale"]]

    with open(report_path, "w") as f:

        f.write("PENALTIES REPORT\n")
        f.write(f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Stale files: {len(stale_files)}\n")
        f.write("=" * 50 + "\n\n")

        if not stale_files:
            f.write("No stale files — no fines!\n")
        else:
            total_fine = 0.0

            for file in stale_files:
                f.write(f"File: {file['name']}\n")
                f.write(f"Days old: {file['days_old']}\n")
                f.write(f"Fine: ${file['fine']:.2f}\n")
                f.write("-" * 40 + "\n")
                total_fine += file["fine"]

            f.write(f"\nTOTAL FINES: ${total_fine:.2f}\n")

    return report_path


def main():

    print(f"\nScanning: {PROJECT_FOLDER}")

    files = scan_folder(PROJECT_FOLDER)

    if not files:
        print("No files found. Exiting.")
        return

    make_reports_folder()

    timestamp = get_timestamp()

    audit_path    = write_audit_report(files, timestamp)
    penalties_path = write_penalties_report(files, timestamp)

    print(f"Audit report: {audit_path}")
    print(f"Penalties report: {penalties_path}\n")


if __name__ == "__main__":
    main()
