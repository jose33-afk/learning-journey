#include <stdio.h>

//Faça um programa que peça ao usuário um caracter e diga se é uma vogal ou não.

int main() {
    char voga, c = 0;

    printf("VOGAL??\n"
           "--------------\n");
    printf("Digite uma letra: ");
    voga = getchar();   

    switch(voga) {
        case 'A':
        case 'a': //Da pra por duas condiçoes 
            c++; 
            break;
        case 'E':
        case 'e':
            c++;
            break;
        case 'I':
        case 'i':
            c++;
            break;
        case 'O':
        case 'o':
            c++;
            break;
        case 'U':
        case 'u':
            c++;
    }

    printf("--------------------\n");
    if (c >= 1) {
        printf(" %c, e uma vogal!", voga);
    } else {
        printf(" %c, nao e uma vogal!", voga);
    }
    
    printf("\n--------------------\n");
    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}