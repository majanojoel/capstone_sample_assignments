#include <stdio.h>

int factorialNum = 5;

int globalFactorial(){
    int currNum = factorialNum;
    factorialNum--;
    if(factorialNum==0) return 1;
    return currNum*globalFactorial();
}

// int factorial(int a){
//     if(a==0) return 1;
//     return a*factorial(a-1);
// }

int main(void){
    printf("My recursion program!\n");
    int result = globalFactorial();
    printf("Factorial: %d\n", result);
    return 0;
}