#include <stdio.h>

/*15) Faça um programa que peça ao usuário dois números inteiros e apresente o resultado na
multiplicação entre os dois números sem utilizar a operação de multiplicação.*/

int main() {
    int quant_vs, valor, c, resul=0;

    printf("Qual valor a ser multiplicado?  ");
    scanf("%i", &valor);
    printf("Quantas vezes? x");
    scanf("%i", &quant_vs);

    for (c=1; c<=quant_vs; c++) {
        resul += valor;
    }

    printf("\nRESULTADO\n"
           "%i  x %i = %i", valor, quant_vs, resul);

    printf("\nPressione Eneter para continuar...");
    getchar();
    getchar();
    
    return 0;
}