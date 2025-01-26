#include <stdio.h>
#include <locale.h>
#include <string.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    float preco_produto;
    int esc;
    char epoca[20];

    printf("Digite o preço de um produto R$");
    scanf("%f", &preco_produto);
  
    printf("\n\n\t       ESCOLHA UM PERÍODO  \n"
           "\t================================\n"
           "\t   1\tCarnaval         [+10]\n"
           "\t   2\tFérias Escolares [+20]\n"
           "\t   3\tDia das criaças  [+5]\n"
           "\t   4\tBlack Friday     [-30]\n"
           "\t   5\tNatal            [-5]\n"
           "\t================================\n"
           "\tDigite sua opçao => ");
    scanf("%i", &esc);

    printf("\n\n-------------------------------------------------------------\n");

    switch (esc) {
        case 1:
            preco_produto += preco_produto * 10 /  100;
            strcpy(epoca, "Carnaval");
            break;
        case 2:
            preco_produto += preco_produto * 20 / 100;
            strcpy(epoca, "Férias");
            break;
        case 3:
            preco_produto += preco_produto * 5 / 100;
            strcpy(epoca, "Dia das criaças");
            break;
        case 4:
            preco_produto -= preco_produto * 30 / 100;
            strcpy(epoca, "Black Friday");
            break;
        case 5:
            preco_produto -= preco_produto * 5 / 100;
            strcpy(epoca, "Natal");
            break;
        default:
            printf("Em épocas assim, mantenha o preço do produto em R$%.2f.\n", preco_produto);
    }
 
    if (esc>0 && esc<=5) {
        printf("Na época das %s, o preço do produto vai para R$%.2f.\n", epoca, preco_produto);
    }

    printf("-------------------------------------------------------------\n");
    printf("VOLTE SEMPRE!\n");
}