import csv
import sys

def main():
    # بررسی تعداد آرگومان‌ها
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # خواندن فایل CSV
    with open(sys.argv[1], "r") as csvfile:
        reader = csv.DictReader(csvfile)
        people = list(reader)

    # خواندن فایل DNA
    with open(sys.argv[2], "r") as dnafile:
        dna_sequence = dnafile.read()

    # استخراج نام STRها از فایل CSV
    str_list = reader.fieldnames[1:]

    # محاسبه تعداد تکرار STRها در دنباله DNA
    str_counts = {}
    for str_name in str_list:
        str_counts[str_name] = longest_match(dna_sequence, str_name)

    # مقایسه با داده‌های CSV
    for person in people:
        match = True
        for str_name in str_list:
            if int(person[str_name]) != str_counts[str_name]:
                match = False
                break
        if match:
            print(person["name"])
            return

    # اگر هیچ مطابقتی یافت نشد
    print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    max_run = 0
    current_run = 0
    subsequence_length = len(subsequence)

    for i in range(len(sequence)):
        if sequence[i:i+subsequence_length] == subsequence:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run

if __name__ == "__main__":
    main()
