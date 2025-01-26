#include <stdio.h>
void main() {
    char nome1[30], nome2[30], nome3[30];
    char sexo1, sexo2, sexo3;
    float nota1, nota2, nota3;

    printf("Cadastrando a primeira pessoa:\n");
    printf("-----------------------------\n");
    printf("NOME: ");
    gets(nome1);
    printf("SEXO [M/F]: ");
    sexo1 = getchar();
    printf("NOTA: ");
    scanf("%f", &nota1);

    printf("Cadastrando a Segunda pessoa:\n");
    printf("-----------------------------\n");
    printf("NOME: ");
    fflush(stdin);  //Para n dar problema com string quando ler outro.
    gets(nome2);
    printf("SEXO: [M/F]: ");
    sexo2 = getchar();
    printf("NOTA: ");
    scanf("%f", &nota2);

    printf("Cadastrando a Teceira pessoa:\n");
    printf("-----------------------------\n");
    printf("NOME: ");
    fflush(stdin); 
    gets(nome3);
    printf("SEXO [M/F]: ");
    sexo3 = getchar();
    printf("NOTA: ");
    scanf("%f", &nota3);

    printf("------------------------------------\n");
    printf("%s%23s%9s", "NOME", "SEXO", "NOTA");
    printf("\n%-15s\t\t%-3c\t%.2f\n",nome1, sexo1, nota1);
    printf("%-15s\t\t%-3c\t%.2f\n",nome2, sexo2, nota2);
    printf("%-15s\t\t%-3c\t%.2f\n",nome2, sexo2, nota3);
    printf("------------------------------------");
}

