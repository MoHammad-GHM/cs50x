#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;

    // گرفتن مقدار باقیمانده (حتماً عدد صحیح ≥ 0)
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int coins = 0;

    // محاسبه تعداد سکه‌های 25 سنتی
    coins += cents / 25;
    cents %= 25;

    // محاسبه تعداد سکه‌های 10 سنتی
    coins += cents / 10;
    cents %= 10;

    // محاسبه تعداد سکه‌های 5 سنتی
    coins += cents / 5;
    cents %= 5;

    // محاسبه تعداد سکه‌های 1 سنتی
    coins += cents;

    // چاپ حداقل تعداد سکه‌ها
    printf("%i\n", coins);
}
