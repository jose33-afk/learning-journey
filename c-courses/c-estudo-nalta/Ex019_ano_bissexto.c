#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int ano;
    
    printf("Digite um ano qualquer: ");
    scanf("%i", &ano);

    if ((ano % 4 == 0 && ano % 100 != 0) || (ano % 100 == 0 && ano % 400 == 0)) {
        printf("O ano %i É BISSEXTO!", ano);
    } else {
        printf("O ano %i NÃO É BISSEXTO!", ano);
    }
}