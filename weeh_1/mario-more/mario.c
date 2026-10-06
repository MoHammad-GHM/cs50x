
#include <stdio.h>

int main(void) {
    int height = 0;


    do {
        printf("Height (1-8): ");
        if (scanf("%d", &height) != 1) {


            int c;
            while ((c = getchar()) != '\n' && c != EOF) { }
            height = 0;
        }
    } while (height < 1 || height > 8);


    for (int row = 1; row <= height; row++) {

        for (int s = 0; s < height - row; s++) {
            putchar(' ');
        }


        for (int h = 0; h < row; h++) {
            putchar('#');
        }


        putchar(' ');
        putchar(' ');


        for (int h = 0; h < row; h++) {
            putchar('#');
        }
        putchar('\n');
    }

    return 0;
}
