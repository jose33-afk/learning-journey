#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Elabore um programa que, dado o número do mês, 
//indica quantos dias têm esse mês. Utilize para
//isso a estrutura de seleção switch.
//Obs.: Considere fevereiro como tendo 28 dias.

int main() {
    int mes;

    printf("Dias do mes (\?\?), digite o numero do mes\n"
           "Para saber a quantidade de dias.\n"
           "==========================================\n"
           "Digite o numero do mes: ");
    scanf("%i", &mes);

    //Basciamente n tem um breake, ele sai pulando ate o breake.
    switch (mes) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            printf("Dias:31");
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            printf("Dias:30");
            break;
        case 2:
            printf("Dias:28");
            break;
        default:
            printf("Numero de mes invalido! Tente Novamete..\n");
            system("pause");
            exit(0);
    }

    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}