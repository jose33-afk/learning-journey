#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int esc;
    float reais;
    char o [49], v[35];

    strcpy(o, "================================");
    strcpy(v, "\n\tVALOR NO MOMENTO DO REAL R$5,12\n");

    //Inicio
    printf("\t      CONVERSOR DE MOEDAS\n"
           "================================================\n"
           "Quantos reais deseja converter? R$");
    scanf("%f", &reais);

    //selecionar moeda
    printf("\n\t%s\n"
           "\t|EURO - 1                      |\n"
           "\t|DOLAR AMERICANO - 2           |\n"
           "\t|YEN - 3                       |\n"
           "\t%s\n", o, o);
    printf("\tSelecione a opçao:");
    scanf("%i", &esc);

    switch (esc) {
        case 1:
              printf("%s\tVALOR NO MOMENTO DO EURO R$6,14\n\n"
                     "\t%s\n\tReais convertidos: R$%.2f\n"
                     "\tValor em EUROS: R$%.2f", v, o, reais, reais / 6.14);
              break;
       case 2:
              printf("%s\tVALOR NO MOMENTO DO DOLAR R$5,78\n\n"
                     "\t%s\n\tReais convertidos: R$%.2f\n"
                     "\tValor em dolar: R$%.2f", v, o, reais, reais / 5.78);
              break;
       case 3:
              printf("%s\tVALOR NO MOMENTO DO YEN R$0,037\n\n"
                     "\t%s\n\tReais convertidos: R$%.2f\n"
                     "\tValor em yen: R$%.2f", v, o, reais, reais / 0.037);
              break;
       default:
              printf("\t\nERRO! Não existe essa opçao, Tente novamente...\n");
              system("pause");
              exit(0);
    }

    printf("\n\t%s\n", o);
    system("pause");

    return 0;
}
