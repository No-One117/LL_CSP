


#include <stdio.h>

int main() {
    int age;
    printf("How old are you?: ");
    scanf("%d", &age);
    
    if (age >= 21) {
        printf("You can drink the fun juice :)\n");
    } else if (age >= 18) {
        printf("You can vote, tokyo drift, get a permit, and go to school but you cant drink the fun juice :(.\n");
    } else if (age >= 16) {
        printf("You can tokyo drift and go to school.\n");
    } else if (age >= 15) {
        printf("You can get a permit and go to school.\n");
    } else if (age >= 5) {
        printf("You can go to school.\n");
    } else {
        printf("Stand ready for my arrival, worm.\n");
    }

    return 0;
}




