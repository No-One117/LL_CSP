// LL 6th Expressions notes
#include <stdio.h>

int main(void){
    int a = 5; //take whole numbers
    float pi = 3.14; //take decimal numbers
    double long_pi = 3.141592653589793; // decimals twice as long as float
    char grade = 'A'; //take single characters
    char name[] = " Lucas"; //string is an array of characters

printf("%f\n", 8/3);
printf("%f\n", 8/3.0);

    return 0;
}

//What is the difference between an integer and a float in C?
// An integer is a whole number while a float is a number that can have a decimal
//How does C handle integer division compared to float division?
// C handles integer division by returning only the whole number.
//List the arithmetic operators available in C and their functions.
// The arithmetic operators in C are: + -  * / % <-- modulos
//What is the modulus operator, and how is it used?
// to find the remainder of division
//How do you round a float to the nearest integer in C?
// You can round a float to the nearest integer in C using the round() function
//What is type casting in C? Provide an example of explicit type casting.
// Type casting is the process of converting a variable from one data type to another
//How do compound assignment operators work in C? List three examples.
// Compound assignment operators combine an arithmetic operation with assignment.
//What is the purpose of the math.h library? Name three functions it provides.
// The math.h library provides mathematical functions.
//How do you print a float with a specific number of decimal places using printf()?
// You can print a float with a specific number of decimal places using the format specifier
//What happens when you mix integer and float operations in C?
// the integer is promoted to a float