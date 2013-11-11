#include <stdio.h>
#include <gmp.h>


int main(int argc, char *argv[]) {
    mpz_t test, exponent, base, modulus;
    char a;
    a = 'a';
    
    mpz_init_set_str(exponent, "123", 10);
    mpz_init_set_str(base, "57", 10);
    mpz_init_set_str(modulus, "132", 10);
    mpz_init (test);


    printf("%c\n", a);
    
    mpz_powm(test, base, exponent, modulus);
    gmp_printf("%Zd\n", test);
    
    return 0;
    }
