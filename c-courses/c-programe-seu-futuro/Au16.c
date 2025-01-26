#include <stdio.h>

// Aula 16 operador sizeof
//sizeof x sizeof(int)

int main () {
    
    float x;

    printf("Tamanho em memoria em bytes: %d byte\n", sizeof x); //ou tamanho da variavel, aqui o parenteses é opcional, ja no de baixo é obrigatorio.
    printf("Tamanho em memoria de um int: %d byte", sizeof(int));  //Basicamente diz a quantidades de bytes que um tipo possui na memoria do pc.

    return 0;
}