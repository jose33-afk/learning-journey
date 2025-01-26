#include <stdio.h>

/*Elabore um programa em C para ler do teclado um valor inteiro entre 1 e 10 e apresentar a
tabuada. 7 * 1 = 7*/

int main() {
    int num, cont;

    printf("   TABUADA\n"
           "=============\n"
           "Tabuada do? ");
    scanf("%i", &num);
    printf("------------\n");

    for (cont = 1; cont <= 10; cont++) {
        printf(" %i * %i = %i\n", num, cont, num * cont);
    }
    
    printf("------------\n");
    printf("Pressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}