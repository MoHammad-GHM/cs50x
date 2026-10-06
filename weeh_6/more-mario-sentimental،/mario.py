def main():
    while True:
        height = get_int("Height: ")
        if 1 <= height <= 8:
            break

    for i in range(1, height + 1):
        # چاپ فاصله‌های سمت چپ
        print(" " * (height - i), end="")
        # چاپ نیم‌هرم اول
        print("#" * i, end="")
        # چاپ فاصله بین دو نیم‌هرم
        print("  ", end="")
        # چاپ نیم‌هرم دوم
        print("#" * i)

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 8.")

if __name__ == "__main__":
    main()
