#include "utility.h"

int search(int* a, int sz, int i) {
    /* fill me in */
    return 0;
}

int main() {
    int sz;
    int* a = read_ints(stdin, &sz);
    printf("%d\n", search(a, sz - 1, a[sz - 1]));
}
