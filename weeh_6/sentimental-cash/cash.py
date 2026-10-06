def main():
    # دریافت ورودی از کاربر
    while True:
        dollars = get_float("Change owed: ")
        if dollars >= 0:
            break

    # تبدیل دلار به سنت
    cents = round(dollars * 100)

    # محاسبه تعداد سکه‌ها
    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    # چاپ مجموع تعداد سکه‌ها
    print(quarters + dimes + nickels + pennies)

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")

if __name__ == "__main__":
    main()
