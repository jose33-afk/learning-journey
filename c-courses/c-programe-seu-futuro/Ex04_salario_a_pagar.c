#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int  dias_trabalhados, impo;
    float valor_diaria, salario;
    char nome_funciona[30];

    printf("============================================\n");
    printf("Nome do Funcionario: ");
    gets(nome_funciona);
    printf("Valor da diaria de %s: R$", nome_funciona);
    scanf("%f", &valor_diaria);
    printf("Valor do imposto de renda? %%");
    scanf("%i", &impo);
    printf("============================================\n");
    printf("\n--------------------------------------------\n");

    printf("Dias Trabalhados:");
    scanf("%i", &dias_trabalhados);
    printf("--------------------------------------------\n");
    printf("\n============================================\n");

    salario =  dias_trabalhados * valor_diaria;
    salario -= salario * impo / 100;

    printf("Nome:%s\n"
           "Dias Trabalhado:%i\n"
           "Salario: R$%.2f\n", nome_funciona, dias_trabalhados, salario);
    printf("============================================\n");
    
    system("pause");
    return 0;
}