#include <stdio.h>
#include <locale.h>

/*
Faça um programa que, dado três valores a, b e c, verifique se eles podem ser os comprimentos
dos lados de um triângulo. Caso positivo, seu programa deve informar também se o triângulo é
equilátero, isósceles ou escaleno. Caso contrário, seu programa deve escrever a mensagem ?Não
formam um triângulo?.
*/

int main() {
    setlocale(LC_ALL, "Portuguese");
    int lados[3], c, b=0;

    printf("    FORMA UM TRIAGOLO\n"
           "--------------------------\n"
           "Digite o comprimento dos tres\n"
           "lados para verificar se e um triangolo.\n"
           "=======================================\n");

    for (c = 0; c <= 2; c++) {
        ++b;
        printf("Digite o %iº lado: ", b);
        scanf("%i", &lados[c]);
    }
    
    printf("---------------------------------\n");
    if ((lados[0] + lados[1]) > lados[2] && (lados[0] + lados[2]) > lados[1] && (lados[1] + lados[2]) > lados[0]) {
        if (lados[0] == lados[1] && lados[0] == lados[2]) {
            printf("Triângolo equilátero");
        }else if ((lados[0] == lados[1]) || (lados[0] == lados[2]) || (lados[1] == lados[2])) {
            printf("Triângolo Isósceles");
        }else {
            printf("Triângulos Escalenos");
        }
    } else {
        printf("Os três lados não formam um triângulo");
    }
    printf("\n---------------------------------\n");

    printf("Pressione Enter para fechar...\n");
    getchar();
    getchar();

    return 0;
}