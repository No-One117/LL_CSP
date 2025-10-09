// LL 6th Silly Sentences

#include <stdio.h>

int main() {
    char word1[51];
    char word2[51];
    char word3[51];

    printf("Enter a noun: ");
    scanf("%50s", word1);

    printf("Enter an adjective: ");
    scanf("%50s", word2);

    printf("Enter a verb: ");
    scanf("%50s", word3);

    printf("The %s %s was scared to %s on Tuesday.\n", word2, word1, word3);

    return 0;
}