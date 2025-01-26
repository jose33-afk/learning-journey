#include <stdio.h>
#include <stdlib.h>
/*
Escreva um programa em C que lê 5 números inteiros, um por vez. Conte quantos destes valores
são negativos e quantos são positivos. Ao final, imprima na tela a quantidade de números negativos
e positivos.
*/

int main() {
    int num1, num2, num3, num4, num5, cont_posito = 0, cont_negat = 0; //Tem que por zero, senao como ele vai somar mais um com o ++

    printf("Conta a quantidade de numeros POSITIVOS e NEGATIVOS\n"
           "Digitados.\n"
           "=====================================================\n\n");

    //Primeiro
    printf("Digite o primeiro valor: ");
    scanf("%i", &num1);
    if (num1 < 0) ++cont_negat;
    else if (num1 > 0) ++cont_posito;

    //Segundo
    printf("Digite o segundo valor: ");
    scanf("%i", &num2); 
    if (num2 < 0) ++cont_negat;
    else if (num2 > 0) ++cont_posito;

    //Terceiro
    printf("Digite o terceiro valor: ");
    scanf("%i", &num3);
    if (num3 < 0) ++cont_negat;
    else if (num3 > 0) ++cont_posito;  else if (num1 > 0) ++cont_posito;

    //Quarto
    printf("Digite o quarto valor: ");
    scanf("%i", &num4);
    if (num4 < 0) ++cont_negat;
    else if (num4 > 0) ++cont_posito;

    //Quinto
    printf("Digite o quinto valor: ");
    scanf("%i", &num5);
    if (num5 < 0) ++cont_negat;
    else if (num5 > 0) ++cont_posito;

    //Resultado
    printf("\n\t---------------------------------------\n"
           "\t   Quantida de numeros positivos: %i.\n"
           "\t   Quantidade de numeros negativos: %i.\n"
           "\t----------------------------------------\n", cont_posito, cont_negat);

    system("pause");

    return 0;
}