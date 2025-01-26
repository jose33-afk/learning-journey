#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int valor1, valor2;

    printf("Digite o primeiro valor: ");
    scanf("%i", &valor1);
    printf("Digite o segundo valor: ");
    scanf("%i", &valor2);
    printf("------- OPERADOÇOES BITWISE -------\n");
    printf("Calculando %i & %i é igual a %i\n", valor1, valor2, valor1 & valor2);
    printf("Calculando %i | %i é igual a %i\n", valor1, valor2, valor1 | valor2);
    printf("Calculando %i ^ %i é igual a %i", valor1, valor2, valor1 ^ valor2);
}