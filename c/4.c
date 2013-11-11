#include <stdlib.h>
#include <stdio.h>

_Bool is_palindrome(char *test_string) {
    int test_string_length, i;
    /*printf("%ld\n", sizeof(test_string));*/
    test_string_length = sizeof(test_string) / sizeof(char);
    
    for (i = 0; i <= test_string_length / 2; i++) {
        if (test_string[i] != test_string[test_string_length - i]) {
            return 0;
        }
    }
    
    return 1;
}

int main() {
    int number_1, number_2, test_palindrome, max_palindrome;
    char *palindrome_string;
    
    for (number_1 = 100; number_1 < 1000; number_1++) {
        for (number_2 = 100; number_2 < 1000; number_2++) {
            test_palindrome = number_1 * number_2;
            
            palindrome_string = (char *) malloc(sizeof(test_palindrome) / sizeof(int));
            sprintf(palindrome_string, "%d", test_palindrome);
        
            if (max_palindrome < test_palindrome) {
                if (is_palindrome(palindrome_string) == 1) {
                    max_palindrome = test_palindrome;
                }
            }
        }
    }
    printf("%d\n", max_palindrome);
    return 0;
}
