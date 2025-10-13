// LL 6th My Family practice

#include <stdio.h>

int main() {

    const char* names[] = {"Mom", "Dad", "Morgan", "Parker", "Vernon Law"};
    int size = sizeof(names) / sizeof(names[0]);

    for(int i = 0; i < size; i++) {
        printf("Hello, %s!\n", names[i]);
    }

    return 0;
}