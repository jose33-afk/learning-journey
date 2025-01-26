#include <stdio.h>

/*
    aula 19 - operador long para o tipo in 
    %lli / %lld  //%li long int | %lli long long int
*/

int main () {
    
    long long int x = 2147483647; //Tem que por duas vezes, e limite é duas vezes

    printf("tamanho de x em bytes: %i\n", sizeof x);
    printf("Valor de x: %i\n", x);
    x++; //x = x + 1
    printf("Valor de x: %lli", x);

    return 0;
}