#include <stdio.h>

int main(void)
{
    char * string = "hello there";
    char str2[] = "hello there 2";
    int i;

    for (i=0; str2[i] != '\0'; i++)
    {
        if (str2[i] == 'e')
        {
            str2[i] = '3';
        }
    }

    printf("%s\n", str2);
}