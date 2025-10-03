// LL 6th Variables notes
#include <stdio.h>

int main(void){
    int num = 4;
    float pi = 3.14;
    char grade = 'A';//will only hold one character
    char name[] = " Lucas";//string is an array of characters
    //bool passing = true;
    printf("%d", num);

    return 0;
}

//What is the main difference between declaring variables in Python and C?
// the main difference is that in C you have to specify the data type of the variable when you declare it, while in Python you do not have to specify the data type
//In C, what is the purpose of specifying a data type when declaring a variable?
// the purpose of specifying a data type when declaring a variable in C is to tell the compiler what kind of data the variable will hold.
//How do you declare and initialize an integer variable named "age" with the value 25 in C?
// you would declare it like this: int age = 25;
//What is the difference between printf() and scanf() functions in C?
// the printf() function is used to print output to the console, while the scanf() function is used to get input from the user.
//How do you add comments in C?
// this is a comment and a multi-line comment is like this ( /* this is a multi-line comment */ )
//What is the purpose of the #include <stdio.h> line at the beginning of a C program?
// the purpose of the #include <stdio.h> line at the beginning of a C program is to include the standard input/output library, which contains functions like printf() and scanf().
//In C, what is the significance of the main() function?
// the significance of the main() function in C is that it is the entry point of the program, where the execution of the program begins.
//What is the difference between %d and %f format specifiers in printf()?
// the %d format specifier is used to print integers, while the %f format specifier is used to print floating-point numbers.
//How do you print a newline character in C?
// to print a newline character in C, you use the \n escape thingy
//What is the purpose of the & symbol when using scanf() to get user input?
// to get user input is to provide the address of the variable where the input value will be stored.
//How do you declare a constant in C? Provide an example.
// you declare a constant in C using the const keyword, const int max_age = 100;