#include <stdio.h>

long fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

int main() {
    int n = 30;
    printf("fib(%d) = %ld\n", n, fib(n));
    return 0;
}

