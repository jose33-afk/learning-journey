#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <stdlib.h>

/*Escreva um programa em C que funcione como uma calculadora. O programa deve apresentar
um menu ao usu�rio da seguinte forma:
1 ? Somar
2 ? Subtrair
3 ? Multiplicar
4 ? Dividir
0 ? Sair*/

int main() {
    setlocale(LC_ALL, "Portuguese");
    int n[2], esc, c;

    printf("    CALCULADORA\n"
           "====================\n"
           " 1 - Somar\n"
           " 2 - Subtrair\n"
           " 3 - Multiplica�ao\n"
           " 4 - Dividir\n"
           " 5 - Sair\n"
           "===================\n"
           "Digite sua op�ao => ");
    scanf("%i", &esc);
   
    if (esc<=0 || esc>=5){
        if (esc==5)
            printf("\nSaindo da calculadora..\n");
        else {
            printf("\nErro opcao Invalida!!\n"
                   "Tente novamente...\n\n"
                   "Saindo da calculadora..");
        }
        printf("\nPrecione Enter para continuar....");
        getchar();
        getchar();
        exit(0);
    }

    printf("\nSomente numeros positivos!!\n\n");
    for (c=0; c<=1; c++) {
        printf("Digite o %i� valor: ", c + 1); //Nao interfere no c++.
        scanf("%i", &n[c]);
        if (n[c] == 0) {
            printf("N�o esta disponivel opera�oes com zero!\n");
            do {
                printf("Digite o %i� valor:", c + 1);
                scanf("%i", &n[c]);  
                if (n[c]==0) printf("Erro! digite novamente...\n");
            } while(n[c]==0);
        } 
    }

    printf("\n-----------------------\n");
    if (esc==1) printf("Soma: %i + %i = %i.", n[0], n[1], n[0] + n[1]); //N�o � poss�vel modificar uma vari�vel diretamente dentro de uma express�o do printf (como n[0] + n[1]), 
    else if (esc==2) printf("Subritrair: %i - %i = %i", n[0], n[1], n[0] - n[1]); //pois ela � apenas avaliada naquele momento para exibi��o.
    else if (esc==3) printf("Multiplica�ao: : %i x %i = %i", n[0], n[1], n[0] * n[1]);
    else if (esc==4) printf("Divisao: : %i / %i = %i", n[0], n[1], n[0] / n[1]);
        
    printf("\n-----------------------\n\n"                                                              
           "VOLTE SEMPRE!!!\n");

    printf("Precione Enter para continuar....");
    getchar();
    getchar();

    return 0;
}