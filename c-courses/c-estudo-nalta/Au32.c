#include <stdio.h>
void main() {
    //Condiçoes multiplas
    int n;

    printf("Digite um numero: ");
    scanf("%i", &n);

    switch (n) {  //Basicamente um escolha || so funciona pra valores char e int.
        case 1: //Dois pontos aqui, n usar ;
            printf("Um");
            break; //Tem que por, funcao? é sai do switch. senao da erro.
        case 2:
            printf("Dois");
            break;
        case 3:
            printf("Tres");
            break;
        case 4:
            printf("Quatro");
            break;
        default: //Outro. tbm opcional.
            printf("Erro!"); //break aqui é opcional, ja que ele é o ultimo, ja iria sair de qualquer jeito.
    }
    printf("\nACABOU!");
}