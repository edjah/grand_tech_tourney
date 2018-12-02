#include "utility.h"

char* reverse(char* s) {
    /* fill me in */
    return 0;
}

int main() {
    int sz;
    char** a = read_strings(stdin, &sz);
    char* s = reverse(a[0]);
    printf("%s\n", s);
}
