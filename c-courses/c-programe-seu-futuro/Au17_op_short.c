#include <stdio.h>

/*
    operador short para tipo int 
    intervalo: -32.768 ate 32.767 limite, ate aqui é ok de usar o shot int, se passar tem que ser o int normal senao vai dar erro.
    %hi ou %d
*/

int main () {
    
    short int x = 32767;

    printf("Valor de x: %i\n", x);
    x++; //x = x + 1
    printf("Valor de x: %i", x);

    return 0;
}