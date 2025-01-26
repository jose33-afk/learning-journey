#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
int main() {
    setlocale(LC_ALL, "Portuguese");
    int valor1, valor2;
    char escolha;

    printf("VALOR 1 = ");
    scanf("%i", &valor1);
    printf("VALOR 2 = ");
    scanf("%i", &valor2);
    printf("===================\n"
           "+\tAdiçao\n"
           "-\tSubtraçao\n"
           "*\tMultiplicaçao\n"
           "/\tDivisão\n"
           "===================\n"
           "Digite sua opçao => ");
    fflush(stdin);  //Quando der erro de ler variavel testa com fflush.
    escolha = getchar();
    printf("--------------------------------------------------------------------\n");

    switch (escolha) {
        case '+': //Char '' e n ""
            printf("O resultado de %i + %i é igual a %i.", valor1, valor2, valor1 + valor2);
            break;
        case '-':
            printf("O resultado de %i - %i é igual a %i.", valor1, valor2, (int)valor1 - valor2);
            break;
        case '*':
            printf("O resultado de %i - %i é igual a %i.", valor1, valor2, valor1 * valor2);
            break;
        case '/':
            printf("O resultado de %i - %i é igual a %.2f.", valor1, valor2, valor1 / (float)valor2);
            break;
        default:
            printf("Não foi possivel fazer a operaçao. Tente Novamente.");
    }

    printf("\n--------------------------------------------------------------------\n"
           "VOLTE SEMPRE!\n");

        printf("Precione Enter para continuar....");
        getchar();
        getchar();
        return 0;
}
