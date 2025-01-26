#include <stdio.h>
#include <locale.h>

/*18) Foi feita uma pesquisa entre os habitantes de uma região e foram coletados os dados de idade,
sexo (M/F) e salário de X pessoas (x deve ser informado pelo usuário). Faça um algoritmo que
informe:
a) a média de salário do grupo;
b) a maior e a menor idade do grupo;
c) a quantidade de mulheres com salário até R$2000,00.*/

int valida(int idade) { 
    do {
        printf("Idade: ");
        scanf("%i", &idade);
        
        if (idade > 70) printf("Limite exedido.\nMaior que 70 anos.\n");
        else if (idade < 14) printf("idade minima n atingida.\nIdade minima 14 anos.\n");
    
    } while(!(idade >= 14 && idade <= 70));
    return idade;
}

int validasx(char sexo) {
    do {
        printf("Sexo [F/M]: ");
        scanf(" %c", &sexo);
        if (!(sexo == 'M' || sexo == 'm') && !(sexo == 'F' || sexo == 'f')) printf("ERRO! Tente novamente.\n");
    } while (!(sexo == 'M' || sexo == 'm') && !(sexo == 'F' || sexo == 'f'));
    return sexo;
}

int main() {
    setlocale(LC_ALL, "Portuguese");
    int idade[3], q_pessoas, c, q_msla=0;
    char sexo;
    float salario[2];

    salario[1] = 0;

    printf("Quantas pessoas vão participar da pesquisa ?");
    scanf("%i", &q_pessoas);

    for (c=0; c<q_pessoas; c++) {
        printf("\n%iº Participante\n"
               "-----------------\n", c+1);  
        
        sexo = validasx(sexo);
        idade[0] = valida(idade[0]);

        printf("Digite o salario: R$"); 
        scanf("%f", &salario[0]);
        salario[1] += salario[0];
        
        if (c==0){
            idade[1] = idade[0]; //Primeira idade
            idade[2] = idade[0];
        }
        if (idade[0] < idade[1]) idade[1] = idade[0]; //Menor idade.l
        if (idade[0] > idade[2])idade[2] = idade[0]; //Maior idade.
        if ((sexo == 'F' || sexo == 'f') && salario[0] <= 2000) q_msla++;
        
    }
    
    printf("\n\n----------------------------------------------------\n");
    printf("Media de salario do grupo de %i pessoas.\nMédia:%.2f\n", q_pessoas, salario[1] / q_pessoas);
    printf("Menor idade: %i\n", idade[1]);
    if (!(idade[1] == idade[2])) printf("Maior idade: %i\n", idade[2]);
    if (q_msla > 0) printf("Quantidade de mulheres com salario até R$2000,00:%i\n", q_msla);
    printf("----------------------------------------------------\n");
    
    printf("Pressione Enter para fechar...\n");
    getchar();
    getchar();

    return 0;
}