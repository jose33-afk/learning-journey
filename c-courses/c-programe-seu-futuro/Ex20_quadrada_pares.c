#include <stdio.h>

//Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N,
//inclusive N, se for o caso.

int main() {
    int num, c;

    printf("Digite um valor inteiro: ");
    scanf("%i", &num);
    printf("quadrado dos valores pares\n"
              "=======================\n");

    for (c = 2; c <= num; c+=2){
        printf("%i  = %i\n", c, c * c);
    }

    printf("\nPressione Enter para continuar..");
    getchar();
    getchar();

    return 0;
}