// LL 6th Financial Calculator update

#include <stdio.h>

float getInput(const char prompt[]) {
    float value;
    printf("%s", prompt);
    scanf("%f", &value);
    return value;
}

int calculatePercent(float income, float expense) {
    return (int)((expense / income) * 100);
}

int main() {
    float income, rent, utilities, groceries, transportation;
    float savings, spending;
    int percent;

    income = getInput("What is your monthly income: ");
    rent = getInput("What is your monthly rent/mortgage: ");
    utilities = getInput("What is your monthly utilities: ");
    groceries = getInput("What is your monthly groceries: ");
    transportation = getInput("What is your monthly transportation: ");

    printf("\nYour rent is $%.2f and that is %d%% of your income.\n", rent, calculatePercent(income, rent));
    printf("Your utilities are $%.2f and that is %d%% of your income.\n", utilities, calculatePercent(income, utilities));
    printf("Your groceries are $%.2f and that is %d%% of your income.\n", groceries, calculatePercent(income, groceries));
    printf("Your transportation is $%.2f and that is %d%% of your income.\n", transportation, calculatePercent(income, transportation));

    savings = income * 0.10f;
    float totalExpenses = rent + utilities + groceries + transportation + savings;
    spending = income - totalExpenses;

    printf("\nYou should save $%.2f a month, that is 10% of your income.\n", savings);
    printf("You have $%.2f of spending money each month!\n", spending);

    return 0;
}

