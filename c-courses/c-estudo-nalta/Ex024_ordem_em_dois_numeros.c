#include <stdio.h>
void main() {
    int num, num2;

    printf("Me diga dois numeros e eu colocarei\n"
           "os dois em ordem crescente.\n\n"
           "Primeiro numero: ");
    scanf("%i", &num);
    printf("Segundo numero: ");
    fflush(stdin);
    scanf("%i", &num2);

    if (num>num2) printf("Os numeros em ordem sao %i e %i", num2, num);
    else if (num2>num) printf("Os numeros em ordem sao %i e %i", num, num2);
}