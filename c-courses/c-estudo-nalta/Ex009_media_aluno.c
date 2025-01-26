#include <stdio.h>
#include <locale.h>

// << EX009 - Média do aluno >>
void main () {
    setlocale(LC_ALL,"Portuguese");
    char nome[50];
    float nota1, nota2, media;

    printf("Nome do aluno: ");
    gets(nome);
    printf("Nota 1: ");
    scanf("%f", &nota1);
    printf("Nota 2: ");
    scanf("%f", &nota2);
    media = (nota1 + nota2) / 2;
    printf("O aluno %s tirou notas %.2f e %.2f e ficou com a média %.2f.", nome, nota1, nota2, media);
}