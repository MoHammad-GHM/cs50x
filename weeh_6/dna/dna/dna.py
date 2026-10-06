import csv
import sys

def main():
    # بررسی تعداد آرگومان‌های خط فرمان
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
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run

if __name__ == "__main__":
    main()
