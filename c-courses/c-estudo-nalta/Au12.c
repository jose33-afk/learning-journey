#include <stdio.h>
#define A "Joao" // primeira forma
void main() {
    int total = 8; //variavel normal sempre por em minusculos, e constante em maiusculo pra facilitar a vida.
    total = 25;
    const N = 8; // Segunda forma de declarar uma Constante, constante n muda o valor, se tentar mudar o valor o programa da erro N = 25.
    printf("Variavel = %i\nConstante %i", total, N);
    printf("%s", A);
}