#include <stdio.h>
#include  <locale.h>
#include <string.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    float distancia, preco_passagem;
    char flase[20];

    printf("======== TABELA DE PREÇOS ========"
           "\nViagens até 200 Km\tR$0.50/Km\n"
           "A partir de 200 Km\tR$0.35/Km\n"
           "----------------------------------\n"
           "Distância total da viagem, em Km:");
    scanf("%f", &distancia);

    if (distancia <= 200) {
        preco_passagem = distancia * 0.50;
        strcpy(flase, "R$0,50/Km");   
    } else {
        preco_passagem = distancia * 0.35;
        strcpy(flase, "R$0,35/Km");
    }

    printf("Uma viagem de %.1f Km vai custar %s", distancia, flase);
    printf("\nValor Total: R$%.2f.", preco_passagem);
}

//05/11/2024