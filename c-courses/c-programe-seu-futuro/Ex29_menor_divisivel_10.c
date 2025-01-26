#include <stdio.h>
#include <locale.h>

/*16) Faça um programa para encontrar o menor número inteiro que seja divisível por todos os
números inteiros entre 1 e 10.
*/

int main() {
    setlocale(LC_ALL, "Portuguese");
    int cont1, cont2, divi=0, menor_valor=0, intervalo;

    printf("Verificar se existe um valor divisivel por 1,2.. ate 10.\n"
           "---------------------------------------------------------\n"
           "Intervalo:");
    scanf("%i", &intervalo);
    printf("\nRESULTADO\n"
           "---------------\n");
           
    for (cont2=1; cont2<intervalo; cont2++) {
        divi = 0; 
        for (cont1=1; cont1<11; cont1++) {
            if (cont2 % cont1 == 0) divi++;
        }

        if (divi == 10) {
            if (menor_valor == 0) menor_valor = cont2; 

            if (cont2 < menor_valor) { 
                menor_valor = cont2;
            }
        } 
    }

    if (menor_valor==0){ 
        printf("Não existe Nenhum! nesse intervalo.\n");
    } else {
        printf("Menor valor divisivel de 1 a 10, em um intervalo de %i!\n"
               "Valor:%i\n",intervalo, menor_valor);
    }
    printf("---------------\n");
    
    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();
    
    return 0;
}