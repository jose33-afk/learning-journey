#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    float valor, desct;

    printf("Qual foi o valor das compras? R$");
    scanf("%f", &valor);
    printf("----------------------------\n");
    printf("Você comprou R$%.2f na nossa loja.\n", valor);

    if (valor>500) {
        desct = valor * 10 / 100;
        printf("========== ATENÇÃO ==========\n");
        printf("Por fazer mais de R$500,00 em compras, você vai receber R$%.2f de desconto\n"
               "O valor a ser pago é R$%.2f! ", desct, valor - desct);
    }

    printf("Volte sempre!\n"); 
    printf("----------------------------");
}