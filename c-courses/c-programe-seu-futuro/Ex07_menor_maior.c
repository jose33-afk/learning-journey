#include <stdio.h>

//Escreva um programa em C que leia três valores e apresente qual é o maior e qual é o menor.

int main () {
    int num1, num2, num3;
    
    printf("Digite o primeiro valor: ");
    scanf("%i", &num1);
    printf("Digite o Segundo valor: ");
    scanf("%i", &num2);
    printf("Digite o Terceiro valor: ");
    scanf("%i", &num3);

    if (num1 > num2 && num1 > num3) printf("O primeiro valor %i e o maior valor.", num1); // Esse if funciona somente com uma linha de comando.
    else if (num2 > num1 && num2 > num3) printf("O segundo valor %i e o maior valor.", num2);
    else printf("O terceiro valor %i e o maior valor.", num3); 

    return 0;
}