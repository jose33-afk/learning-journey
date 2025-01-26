#include <stdio.h>

// Comdiçoes compostas
void main() {
    int n;
    
    printf("Digite um valor: ");
    scanf("%i", &n);
    
    if (n % 2 == 0) {
        printf("O numero %i e um numero par!", n);
    } else {
        printf("O numero %i e um numero Impar!", n);    
    }

}