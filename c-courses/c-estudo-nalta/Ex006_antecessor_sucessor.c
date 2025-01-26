#include <stdio.h>
#include <locale.h>

void main() {
    setlocale(LC_ALL, "Portuguese");
    int num, nump, numa; 

    printf("<<< EX006 - Antecessor e Sucessor >>>\n\n");
    printf("Digite um número: ");
    scanf("%i", &num);
    nump = num + 1;
    numa = num - 1;
    printf("Analizando o número %i, seu antecessor é %i e seu sucessor é %i.", num, numa, nump);
}