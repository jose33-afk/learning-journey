#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int num, oposto;

    printf("Digite um numero: ");
    scanf("%i", &num);

    if (num >= 1){
        printf("O inverso de %i é igual a %.4f", num, 1.0 / num);
    } else {
        oposto = -num;
        printf("o oposto de %i é igual a %i",num, oposto);
    }
    
}