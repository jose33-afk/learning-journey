#include <stdio.h>

//Condiçoes simples aula 28
void main() {
    float vel;
    printf("Digite a velocidade do automovel: ");
    scanf("%f", &vel);

    if (vel > 80) {
        printf("Voce foi multado!\n");
    }

    printf("Se beber, nao dirija!");
}