#include "utility.h"

int* sort(int* a, int sz) {
    /* fill me in */
    return a;
}

int main() {
    int sz;
    int* a = read_ints(stdin, &sz);
    a = sort(a, sz);
    for (int i = 0; i < sz; ++i) {
        printf("%d\n", a[i]);
    }
}
