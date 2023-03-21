#include <stdio.h>
// #include <unordered_map>

// std::unordered_map<int,int> memo{{0,1}, {1,1}};

// int fib(int n){
//     auto it = memo.find(n);
//     if(it != memo.end()) return it->second;
//     return memo[n] = (fib(n-1) + fib(n-2));
// }


int fib(int n){
    if(n == 0 || n == 1) return 1;
    return fib(n-1) + fib(n-2);
}

int main(void){
    printf("My recursion program!\n");
    int result = fib(5);
    printf("Factorial: %d\n", result);
    return 0;
}