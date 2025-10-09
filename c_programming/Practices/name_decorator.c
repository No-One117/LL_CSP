#include <stdio.h>

int main() {
    char name[50];

    printf("What is your name: ");
    fgets(name, sizeof(name), stdin);

    printf(">>>%s<<<\n", name);

    return 0;
}