// LL 6th financial calculator

#include <stdio.h>

int main() {
    float income, rent, utilities, groceries, transportation, savings;

    printf("Monthly income: ");
    scanf("%f", &income);

    printf("Rent: ");
    scanf("%f", &rent);

    printf("Utilities: ");
    scanf("%f", &utilities);

    printf("Groceries: ");
    scanf("%f", &groceries);

    printf("Transportation (Bus pass/car payment): ");
    scanf("%f", &transportation);

    printf("Amount to save: ");
    scanf("%f", &savings);

    float total_expenses = rent + utilities + groceries + transportation;
    float left = income - total_expenses - savings;

    printf("Income: $%f\n", income);
    printf("Total Expenses: $%f\n", total_expenses);
    printf("Savings: $%f\n", savings);
    printf("Left to spend: $%f\n", left);

    return 0;
}