#include <cs50.h>
#include <stdio.h>
int main(void)
{
    // گرفتن نام کاربر
    string name = get_string("Name: ");

    // چاپ سلام
    printf("hello, %s\n", name);
}
