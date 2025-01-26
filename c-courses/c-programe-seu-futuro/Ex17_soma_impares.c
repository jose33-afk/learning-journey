#include <stdio.h>

/*3) Faça um programa que some os números ímpares entre 1 e 1000 e imprima a resposta.
4) Faça um programa que some os números ímpares entre 1 e 1000 e imprima a resposta.
Restrição:
? O bloco de repetição deve executar no máximo 500 vezes.*/

int main() {
    int impa = 0, c; 

    for (c=1; c<=100; c++) {
        if (c % 2 > 0) impa += c; //Tem que inicialiazar impa pra usar os +=, ++ -= etc.
    }

    printf("A soma de 1 a 100 de numeros impares deu: %i", impa);

    return 0;
}