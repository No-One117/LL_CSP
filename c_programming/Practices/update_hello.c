// LL 6th Hello world update
#include <stdio.h>

void greet(const char name[]) {
    printf("Hello %s!\n\n", name);
}

int main() {
    greet("John");
    greet("Morgan");
    greet("Parker");
    greet("Lucas");
    greet("Arthur");

    return 0;
}
