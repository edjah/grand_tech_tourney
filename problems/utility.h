#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

int* read_ints(FILE* file, int* result_length) {
    int sz = 0;
    int capacity = 32;
    int* a = malloc(sizeof(int) * capacity);
    assert(a != NULL);

    char line[65536];
    while (fgets(line, sizeof(line), file) != NULL) {
        if (line[0] == '\n' || line[0] == '\0') {
            continue;
        }
        a[sz++] = atoi(line);
        if (sz == capacity) {
            capacity *= 2;
            a = realloc(a, sizeof(int) * capacity);
            assert(a != NULL);
        }
    }

    *result_length = sz;
    return a;
}

double* read_floats(FILE* file, int* result_length) {
    int sz = 0;
    int capacity = 32;
    double* a = malloc(sizeof(double) * capacity);
    assert(a != NULL);

    char line[65536];
    while (fgets(line, sizeof(line), file) != NULL) {
        if (line[0] == '\n' || line[0] == '\0') {
            continue;
        }

        a[sz++] = atof(line);
        if (sz == capacity) {
            capacity *= 2;
            a = realloc(a, sizeof(double) * capacity);
            assert(a != NULL);
        }
    }

    *result_length = sz;
    return a;
}

char** read_strings(FILE* file, int* result_length) {
    int sz = 0;
    int capacity = 32;
    char** a = malloc(sizeof(char*) * capacity);
    assert(a != NULL);

    char line[65536];
    while (fgets(line, sizeof(line), file) != NULL) {
        a[sz] = malloc(sizeof(char) * (strlen(line) + 1));
        strcpy(a[sz], line);

        if (sz == capacity) {
            capacity *= 2;
            a = realloc(a, sizeof(char*) * capacity);
            assert(a != NULL);
        }
    }

    *result_length = sz;
    return a;
}
