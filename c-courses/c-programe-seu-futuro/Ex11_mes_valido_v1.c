#include <stdio.h>
#include <locale.h>
/*
Faça um programa para ler um número inteiro e verificar se corresponde a um mês válido no
calendário. Caso corresponda, escrever o nome do mês, caso contrário, escrever a mensagem ?Mês
Inválido?.
*/
int main() {
    setlocale(LC_ALL, "Portuguese");
    int m, mes;

    printf("MÊS VALIDO?\n"
           "-------------\n");
    printf("Digite o numero de um mês:");
    scanf("%i", &m);

    if (m >= 1 && m <= 12) {
        printf("\t----------------------\n");
        
        if (m==1) printf("\t  Mês de Janeiro"); //Quando souber variaveis compostas atualizo.
        if (m==2) printf("\t  Mês de Fevereiro"); 
        if (m==3) printf("\t  Mês de Março"); 
        if (m==4) printf("\t  Mês de Abril"); 
        if (m==5) printf("\t  Mês de Maio"); 
        if (m==6) printf("\t  Mês de Junho"); 
        if (m==7) printf("\t  Mês de Julho"); 
        if (m==8) printf("\t  Mês de Agosto"); 
        if (m==9) printf("\t  Mês de Setembro"); 
        if (m==10) printf("\t  Mês de Outubro"); 
        if (m==11) printf("\t  Mês de Novembro"); 
        if (m==12) printf("\t  Mês de Dezembro");  
        
        printf("\n\t----------------------\n");
    } else {
        printf("Não existe mês %i!\n", m);
    }
    	
    printf("\t  Mês de %s", mes);
    printf("Pressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}