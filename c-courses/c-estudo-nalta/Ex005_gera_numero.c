#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

void main() {
    setlocale(LC_ALL, "Portuguese");
    srand(time(NULL));
    int num = rand() % 5 + 1;
    int n;
    printf("<<Ex005 - Será que Você acerta? >>\n\n");
    printf("Vou pensar em um número entre 1 e 5. Tente adivinhar!\n");
    printf("Qual é o seu palpite? ");
    scanf("%i", &n);
    printf("Eu pensei no número %i e você no %i.", num, n);
}