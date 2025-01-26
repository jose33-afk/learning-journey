#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int num;

    printf("Digite um numero qualquer: ");
    scanf("%i", &num);
    printf("O número que você digitou é %s!", (num % 2 == 0)?"Par":"Ímpar");
}