#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    float nota1, nota2, media;

    printf("Primeira nota: ");
    scanf("%f", &nota1);
    printf("Segunda nota: ");
    scanf("%f", &nota2);
    media = (nota1 + nota2) / 2;
    printf("A m�dia do aluno foi %.1f\n", media);
    printf("A sua situa�ao � %s!", (media>=7)?"APROVADO":"REPROVADO");
}