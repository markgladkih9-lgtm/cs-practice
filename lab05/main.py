import os
from logstats import count_levels, top_errors, format_report

def main():
    file_name = input().strip()
    if not os.path.exists(file_name):
        print(0)
        print(0)
        print(0)
        return

    with open(file_name, mode="r", encoding="utf-8") as log:
        counts = count_levels(log)
        
    with open(file_name, mode="r", encoding="utf-8") as log:
        errors = top_errors(log, 3)
        
    broken_count = counts.get("BROKEN", 0)
    error_count = counts.get("ERROR", 0)
    total_parsed = sum(counts.values())
    
    print(total_parsed)
    print(error_count)
    print(broken_count)
    
    report_text = format_report(counts, errors)
    with open("report.txt", mode="w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main()

