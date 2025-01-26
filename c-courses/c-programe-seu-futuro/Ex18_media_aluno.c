#include <stdio.h>

/*
5) Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e
imprima a média semestral. Faça com que o programa só aceite notas válidas (uma nota válida deve
pertencer entre o intervalo de 0 a 10). Cada nota deve ser validada separadamente.
*/

int main() {
    float aluno_notas[2];
    int conf=0;

    do {
        if (conf == 0) {
        printf("Primeira nota: ");
        scanf("%f", &aluno_notas[conf]);
        }
        
        if (conf == 1) {
        printf("Segunda nota: ");
        scanf("%f", &aluno_notas[conf]);
        }
        
        if (aluno_notas[conf] > 0 && aluno_notas[conf] <= 10) ++conf;
        else printf("Nota invalida, verifique se esta no intervalo (1 a 10).\n"
                    "Tente novamente...\n");
        
    } while (!(conf==2)); //Quando for usar o ! tem que por () onde quer q ele funcione.

    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();
    
    return 0;
}