#include <stdio.h>
#include <locale.h>

/*14) Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário a
quantidade de funcionários e o salário de cada funcionário. Ao final, o programa deve imprimir a
média dos salários informados, o salário mais alto e o salário mais baixo.
*/

int main () {
    setlocale(LC_ALL, "Portuguese");
    int quant_func, cont;
    float salario, salario_ba, salario_al, media_sala;

    printf(" EMPRESA X\n"
           "-------------\n"
           "Quantos funcionarios: ");
    scanf("%i", &quant_func);

    for (cont = 0; cont<quant_func; cont++) {
        printf("Informe o %iº salario: ", cont+1);
        scanf(" %f", &salario);
        media_sala += salario;

        if (cont==0) salario_ba = salario; //Primeiro valor
        if (salario>salario_al) salario_al = salario; //Maior salario
        else if (salario<salario_ba) salario_ba = salario; //Menor salario
    }

    printf("\nRESULTADO\n"
           "-------------------------\n");
    if (quant_func < 2) printf("Não é possivel calcular a media com somente 1 funconario!\n");
    else {
        media_sala = media_sala / quant_func;
        printf("Média salárial: R$%.3f,00\n", media_sala);
    }
    printf("-------------------------\n"
           "Maior salário: R$%.3f,00\n"
           "Menor salário R$%.3f,00\n"
           "-------------------------\n", salario_al, salario_ba);
    
    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}