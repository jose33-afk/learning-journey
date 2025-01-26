#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int num, deslo;

    printf("Digite um número: ");
    scanf("%i", &num);
    printf("Digite o deslocamento: ");
    scanf("%i", &deslo);
    printf("------ OPERACOES SHIFT ------\n");
    printf("Calculando %i >> %i é igual a %i\n", num, deslo, num >> deslo);
    printf("Calculando %i << %i é igual a %i", num, deslo, num << deslo);    
}