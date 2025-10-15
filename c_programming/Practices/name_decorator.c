#include <stdio.h>
#include <string.h>

int main() {

    char greeting[100] = ""; 
    char name[50];

    printf("What is your name: ");
    fgets(name, sizeof(name), stdin);

    name[strcspn(name, "\n")] = 0;

    strcat(greeting, name);

    printf(":(:(%s(:(:\n", greeting);

    return 0;
}