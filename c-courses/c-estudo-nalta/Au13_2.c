#include <stdio.h>
/*Lendo um caracter
void main() {
    char r;
    char s;
    printf("Digite so uma letra:");
    r = getchar();  //Para ler só um caracter.
    printf("Digite outra letra:");
    fflush(stdin);  //Tem que por, senao ele conta o enter como um caracter, assim dando erro.
    s = getchar();
    printf("Voce digitou a letra %c e a letra %c", r, s);
}*/
//lendo uma cadeia de caracteres
void main() {
    char nome[30]; // [quantidade de espaços]
    char end[40];
    printf("Digite seu nome:");
    gets(nome);  //Para ler strings, recomendado.
    printf("Digite seu endereco:");
    gets(end);  //Não precisa do fflush(), mas caso de so por.
    printf("Seu nome e \"%s\" e seu endereco é %s", nome, end);
}   