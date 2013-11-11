#include <stdio.h>
#include <time.h>

int main()
{
    clock_t begin, end;
    double time_spent;
    begin = clock();
    long n_minus_two = 1;
    long n_minus_one = 2;
    long n;
    long tally = 2;
    
    while (n_minus_two + n_minus_one < 4000000)
    {
        n = n_minus_two + n_minus_one;
        if (n % 2 == 0)
        {
            tally = tally + n;
        }
        n_minus_two = n_minus_one;
        n_minus_one = n;
    }
    end = clock();
    time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("The sum of the even Fibonacci numbers below 4,000,000 is %ld\n", tally);
    printf("%g\n", time_spent);
}
