#include <stdio.h>
#include <locale.h>

// << EX008 - Alfabeto >>
void main() {
    setlocale(LC_ALL, "Portuguese");
    char letra, antes, depois;

    printf("Digite uma letra:");
    letra = getchar();
    //antes = letra - 1; 
    //depois = letra + 1;
    printf("Antes da letra %c temos a letra %c. Depois temos a letra %c. ",letra, (letra - 1), (letra + 1));
}