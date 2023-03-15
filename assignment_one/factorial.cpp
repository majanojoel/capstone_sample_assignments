#include <stdio.h>

int factorialNum = 5;

int factorial(){
    int currNum = factorialNum;
    factorialNum--;
    if(factorialNum==0) return 1;
    return currNum*factorial();
}

// int factorial(int a){
//     if(a==0) return 1;
//     return a*factorial(a-1);
// }

int main(void){
    printf("My recursion program!\n");
    int result = factorial();
    printf("Factorial: %d\n", result);
    return 0;
}