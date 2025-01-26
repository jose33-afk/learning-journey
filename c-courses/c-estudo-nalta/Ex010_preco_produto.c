#include <stdio.h>
#include <locale.h>

// << EX010 Pre?o do produto >>
void main() {
    setlocale(LC_ALL, "Portuguese");
    char nome_produto[30];
    float preco_produto, desct, novo_valor; 

    printf("Produto:");
    gets(nome_produto);  //Quando poe uma variavel pra ler ele ja pula linha sozinho, n?o ? necessario o \n
    printf("Pre?o de %s: R$", nome_produto);
    scanf("%f", &preco_produto);
    printf("Deconto: (%%) ");
    scanf("%f", &desct);
    novo_valor = preco_produto - (preco_produto * desct / 100);
    printf("O produto %s custava R$%.2f, mas com %.2f%% de desconto, passa a custar R$%.2f.", nome_produto, preco_produto, desct, novo_valor);
}