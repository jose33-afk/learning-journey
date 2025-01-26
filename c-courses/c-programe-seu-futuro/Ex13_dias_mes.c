#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Elabore um programa que, dado o número do mês, 
//indica quantos dias têm esse mês. Utilize para
//isso a estrutura de seleção switch.
//Obs.: Considere fevereiro como tendo 28 dias.

int main() {
    int mes;
    char nome_mes[20];

    printf("Dias do mes (\?\?), digite o numero do mes\n"
           "Para saber a quantidade de dias.\n"
           "==========================================\n"
           "Digite o numero do mes: ");
    scanf("%i", &mes);

    switch (mes) {
        case 1:
            strcpy(nome_mes, "Janeiro");
            mes = 31;
            break;
        case 2:
            strcpy(nome_mes, "Fevereiro");
            mes = 28;
            break;
        case 3:
            strcpy(nome_mes, "Marco");
            mes = 31;
            break;
        case 4:
            strcpy(nome_mes, "Abril");
            mes = 30;
            break;
        case 5:
            strcpy(nome_mes, "Maio");
            mes = 31;
            break;
        case 6:
            strcpy(nome_mes, "Junho");
            mes = 30;
            break;
        case 7:
            strcpy(nome_mes, "Julho");
            mes = 31;
            break;
        case 8:
            strcpy(nome_mes, "Agosto");
            mes = 31;
            break;
        case 9:
            strcpy(nome_mes, "Setembro");
            mes = 30;
            break;
        case 10:
            strcpy(nome_mes, "Outubro");
            mes = 31;
            break;
        case 11:
            strcpy(nome_mes, "Novembro");
            mes = 30;
            break;
        case 12:
            strcpy(nome_mes, "Dezembro");
            mes = 31;
            break;
        default:
            printf("Numero de mes invalido! Tente Novamete..\n");
            system("pause");
            exit(0);
    }

    printf("\nMes de %s.\n"
           "Dias: %i\n", nome_mes, mes);

    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}