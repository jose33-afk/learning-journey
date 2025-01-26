#include <stdio.h>
int main() {
    printf("\nValor retorndo: %i\n", printf("Bom")); //por algum motivo o printf assim retorna a quantidade de caracteres das string, 
    return 0;                                        // e imprime primeiro. e \n etc conta na contagem
}