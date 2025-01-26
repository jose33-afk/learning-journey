#include <stdio.h>

//Faça um programa que imprima na tela todos os múltiplos de 7 entre 1 e 9999.

int main() {
    int mult_num, c;

    printf("Qual valor a ser multiplicado? ==");
    scanf("%i", &mult_num);

    for (c=0; c<=100; c++){
        printf("%i x %i = %i\t", mult_num, c, mult_num * c);
        if (c % 3 == 0) printf("\n");
    }

    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}