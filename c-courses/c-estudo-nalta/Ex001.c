#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    printf("Listagem de Alunos\nNome\t\tNota\n---------------------\nAna Beatriz\t8.5\nBianca Martins\t9.0\n");
    printf("Claúdeo Sá\t5.5\nGiovana Silva\t7.5");
}