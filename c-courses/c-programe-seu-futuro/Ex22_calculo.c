#include <stdio.h>

//Faça um programa que calcule o valor de A, dado por:
//A = 1 + 2 + 3 + 4 + ... + n, onde n é um número inteiro, maior que zero informado pelo usuário.

int main() {
    int num, c, soma = 0;

    printf("Digite um numero inteiro: ");
    do {
        scanf("%i", &num);
        if (num < 1) {
            printf("Valor invalido!, somente numeros positivos\n");
            printf("Digite um numero inteiro: ");
        }
    } while(!(num>=1));

    for (c = 1; c <= num; c++) {
        soma += c; //iniciar a varial com 0!!!
    }

    printf("Soma de todos os valores: %i", soma);
    return 0;
}
