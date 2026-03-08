def show_summary(processed_records):
    total_original  = sum(r["original"]  for r in processed_records)
    total_processed = sum(r["processed"] for r in processed_records)

    print("DATA SYNC DASHBOARD")
    print(f"  {'Source':<10} {'Raw':>8} {'Processed':>12}")

    for r in processed_records:
        print(f"  Source {r['source']:<5} {r['original']:>8} {r['processed']:>12}")

    print(f"  {'TOTAL':<10} {total_original:>8} {total_processed:>12}")
