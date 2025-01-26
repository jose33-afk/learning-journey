#include <stdio.h>
#include <locale.h>

/*13) Faça um programa que peça ao usuário um número inteiro maior que 2 e diga se o número
informado é primo ou não.
*/

int main () {
    setlocale(LC_ALL, "Portuguese");
    int num, t=0, i, primo=0;

    printf("Digite um numero: ");
    scanf("%i", &num);

    if (num > 1) {
        t = num;
        t++;
        for (i=1; i<t; i++){
            if (num % i == 0) primo++;
        }
    }

    if (primo == 2) printf("O número %i, é Primo!", num);
    else printf("O numero %i, não é Primo!", num);

    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}
