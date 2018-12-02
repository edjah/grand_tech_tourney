#include "utility.h"

int two_sum(int* a, int sz, int target) {
    /* fill me in */
    return 0;
}

int main() {
    int sz;
    int* a = read_ints(stdin, &sz);
    printf("%d\n", two_sum(a, sz - 1, a[sz - 1]));
}
