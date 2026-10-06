#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Create a buffer for a block of data
    BYTE buffer[512];

    // Initialize variables for JPEG file handling
    FILE *jpeg = NULL;
    int jpeg_count = 0;
    char filename[8];

    // While there's still data left to read from the memory card
    while (fread(buffer, sizeof(BYTE), 512, card) == 512)
    {
        // Check for JPEG signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous JPEG file if one is open
            if (jpeg != NULL)
            {
                fclose(jpeg);
            }

            // Create a new JPEG file
            sprintf(filename, "%03i.jpg", jpeg_count);
            jpeg = fopen(filename, "w");
            if (jpeg == NULL)
            {
                printf("Could not create JPEG file.\n");
                return 1;
            }
            jpeg_count++;
        }

        // Write data to the JPEG file if one is open
        if (jpeg != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, jpeg);
        }
    }

    // Close any remaining files
    if (jpeg != NULL)
    {
        fclose(jpeg);
    }

    // Close the memory card
    fclose(card);

    return 0;
}
