def main():
    # دریافت متن از کاربر
    text = get_string("Text: ")

    # شمارش تعداد حروف، کلمات و جملات
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # محاسبه شاخص Coleman-Liau
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    # چاپ نتیجه
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(index)}")

def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    count = 0
    for char in text:
        if char in ['.', '!', '?']:
            count += 1
    return count

def get_string(prompt):
    return input(prompt)

if __name__ == "__main__":
    main()
