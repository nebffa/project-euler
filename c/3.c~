#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <gmp.h>

_Bool prime(long n);



int main(int argc, char *argv[]) {
    int i = 1000000;
    long big_number = 600851475143;
    for (; i != 2; i--) {
        if (big_number % i == 0) {
            if (prime(i)) {
                printf("%d\n", i);
                return i;
            }
        }
    }
    
    return 0;
}


_Bool prime(long n) {
    int s = 0, r = 0, a_index = 0;
    int *a_list;
    _Bool composite_part_a = 1, composite_part_b = 1;
    long d = n - 1;
    mpz_t receive, base, exponent, modulus;
    mpz_init(receive);
    mpz_init(base);
    mpz_init(exponent);
    mpz_init(modulus);
    
    if (n == 2) {
        return 1;
    }
    else if (n == 1) {
        return 0;
    }
    else if (n % 2 == 0) {
        return 0;
    }
    
    while (d % 2 == 0) {
        s++;
        d = d / 2;
    }
    
    if (4759123141 <= n && n < 2152302898747) {
        a_list = (int *) malloc(sizeof(int) * 5);
        a_list[0] = 2;
        a_list[1] = 3;
        a_list[2] = 5;
        a_list[3] = 7;
        a_list[4] = 11;
    }
    else if (9080191 <= n && n < 4759123141) {
        a_list = (int *) malloc(sizeof(int) * 3);
        a_list[0] = 2;
        a_list[1] = 7;
        a_list[2] = 61;
    }
    else if (1373653 <= n && n < 9080191) {
        a_list = (int *) malloc(sizeof(int) * 2);
        a_list[0] = 31;
        a_list[1] = 73;
    }           
    else if (4 <= n && n < 1373653) {
        a_list = (int *) malloc(sizeof(int) * 2);
        a_list[0] = 2;
        a_list[1] = 3;
    }
    else if (n == 3) {
        return 1;
    }

    for (a_index = 0; a_index < sizeof(a_list) / sizeof(int); a_index++) {
        mpz_set_si(base, a_list[a_index]);
        mpz_set_si(exponent, d);
        mpz_set_si(modulus, n);
        mpz_powm(receive, base, exponent, modulus);
        
        if (mpz_get_si(receive) != 1) {
            composite_part_a = 1;
        }
        else {
            composite_part_a = 0;
        }
        
        for (r = 0; r < s; r++) {
            mpz_set_si(base, a_list[a_index]);
            mpz_set_si(exponent, pow(2, r) * d);
            mpz_set_si(modulus, n);
            
            mpz_powm(receive, base, exponent, modulus);
            
            if (mpz_get_si(receive) != -1 + n) {
                composite_part_b = 1;
            }
            else {
                composite_part_b = 0;
                break;
            }
        }
        if (composite_part_a == 1 && composite_part_b == 1) {
            return 0;
        }
    }
    return 1;
}
        
