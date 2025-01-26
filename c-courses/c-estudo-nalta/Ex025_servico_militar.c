#include <stdio.h>
#include <time.h>
void main() {
    int ano, ano_nasci, idade, alista;
   
    time_t t;
    time(&t);
    struct tm *data;
    data = localtime(&t);
    ano = data->tm_year + 1900; 

    printf("Atualmente estamos no ano de %i\n"
           "Em que ano voce nasceu? ", ano);
    scanf("%i", &ano_nasci);
    idade = ano - ano_nasci;
    alista = ano_nasci + 18;
    printf("---------------------------------------------------\n");
    printf("Sua idade atual e %i anos.\n", idade);

    if (idade>18) {
        printf("Seu alistamento foi em %i. Ja se passaram %i anos.", alista, ano - alista);
    } else if (idade<18) {
        printf("Seu alistamento sera em %i. Ainda faltam %i anos.", alista, alista - ano);
    } else {
        printf("Voce completa 18 anos extamente em %i. Va se alistar!", ano);
    }

    printf("\n---------------------------------------------------");
}