#include <stdio.h>
#include <locale.h>
#include <time.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int ano_nascimento, idade, ano;

    // Ano atual
    time_t t;
    time(&t);
    struct tm *hora; 
    hora = localtime(&t);
    ano = hora->tm_year + 1900;
    
    printf("Em que ano você nasceu? ");
    scanf("%i", &ano_nascimento);
    idade = ano - ano_nascimento; //idade
    printf("-----------------------------\n");
    printf("Você tem %i anos certo?\n", idade);
    printf("Seja bem-vindo(a) ao Banco Estudonauta!\n");

    if (idade >= 65) {
        printf("=== ATENÇAO! DIRIJA-SE PARA A FILA PREFERENCIAL ===\n");    
    }

    printf("-----------------------------");

}
/*
linha 8
O nome tm para a estrutura (struct) em C é uma convenção da biblioteca padrão (time.h) que define a estrutura para representar informações de data e hora. 
O nome tm é uma abreviação de "time" (tempo, em inglês) e foi escolhido para indicar que a estrutura contém componentes de tempo,
como ano, mês, dia, horas, minutos e segundos.*/