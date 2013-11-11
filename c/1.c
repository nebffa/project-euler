#include <stdio.h>

int main()
{
    int tally;
    int n;
    
    for (n; n < 1000; n++) {
        if (n % 3 == 0 | n % 5 == 0) {
            tally = tally + n;
            }
        }
    
    printf("%d\n", tally);
}
