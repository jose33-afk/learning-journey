#include <stdio.h>
int main() {
    int num1, num3;
    float num2;
    char letra;
    printf("Digite tres valores: ");
    scanf("%i%f%i", &num1, &num2, &num3);

    printf("Valores lidos: %i, %f, %i, %c", num1, num2, num3); //Da pra ler um float e int
    return 0;
}