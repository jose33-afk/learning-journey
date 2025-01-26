#include <stdio.h>

/*
    tamanho de um int memoria
    intervalo: -2.147.483.648 x 2.147.483.648 limite.
*/

int main () {
    
    int x = 2147483647;

    printf("Valor de x: %i\n", x);
    x++; //x = x + 1
    printf("Valor de x: %i", x);

    return 0;
}