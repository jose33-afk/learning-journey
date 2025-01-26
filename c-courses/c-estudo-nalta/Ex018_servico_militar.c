#include <stdio.h>
#include <locale.h>
#include <time.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int ano, ano_nascimento, idade;

    time_t t;
    time(&t);
    struct tm * data;
    data = localtime(&t);
    ano = data->tm_year + 1900;
    
    printf("Atualmente estamos no ano de %i", ano);
    printf("\nEm que ano você nasceu? ");
    scanf("%i", &ano_nascimento);
    idade = ano - ano_nascimento;
    printf("---------------------------------------");
    printf("\nSua idade atual é %i anos.", idade);

    if (idade > 18){
        printf("\nJá fez 18 anos. espero sinceramente que você tenha se alistado.");
    } else{
        printf("\nVocê ainda não tem 18 anos. Não pode se alistar.")
    }
}

//05/11/2024