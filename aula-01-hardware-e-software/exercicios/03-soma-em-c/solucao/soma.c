#include <stdio.h>

int main(void) {
    int a = 5;
    int b = 3;
    int c = a + b;   /* load a, load b, add, store c */

    printf("%d\n", c);
    return 0;
}
