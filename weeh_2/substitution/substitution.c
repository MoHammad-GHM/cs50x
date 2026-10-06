#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // بررسی تعداد آرگومان‌ها
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];

    // بررسی طول کلید
    if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // بررسی معتبر بودن کلید (حروف الفبا و بدون تکرار)
    bool used[26] = {false};

    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }

        int index = tolower(key[i]) - 'a';

        if (used[index])
        {
            printf("Key must not contain repeated characters.\n");
            return 1;
        }

        used[index] = true;
    }

    // گرفتن متن ساده
    string plaintext = get_string("plaintext: ");

    printf("ciphertext: ");

    // رمزگذاری متن
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        char c = plaintext[i];

        if (isupper(c))
        {
            printf("%c", toupper(key[c - 'A']));
        }
        else if (islower(c))
        {
            printf("%c", tolower(key[c - 'a']));
        }
        else
        {
            // کاراکتر غیرالفبایی بدون تغییر
            printf("%c", c);
        }
    }

    printf("\n");
    return 0;
}
