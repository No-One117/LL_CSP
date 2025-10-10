// LL 6th Time of Day practice


#include <stdio.h>
#include <time.h>

int main() {
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);

    int hour = timeinfo->tm_hour;

    if (hour >= 5 && hour < 12) {
        printf("Good morning!\n");
    } else if (hour >= 12 && hour < 18) {
        printf("Good afternoon!\n");
    } else {
        printf("Good evening!\n");
    }

    return 0;
}