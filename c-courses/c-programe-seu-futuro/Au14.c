#include <stdio.h>

//Aula 14 - como ler duas letras e limpar o buffler do teclado com espaço scan().

int main() {
    char a, b;

    printf("Digite uma letras: ");
    scanf("%c", &a); 
    
    printf("Digite uma letras: ");
    scanf(" %c",&b); //Basta por o espaço na frente, que ele ignora ENTER, TAB, ESPAÇO.

    printf("Primeira letra %c segunda %c", a, b);
    return 0;
}