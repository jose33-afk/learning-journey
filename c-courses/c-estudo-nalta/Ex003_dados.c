#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    char nome[40];
    int idade;
    float peso; 
    printf("Qual é o seu nome? ");
    gets(nome);
    printf("Quantos anos vc tem %s?", nome);
    scanf("%i", &idade);
    printf("Qual é o seu peso? ");  //Quando muda o idioma pra portugues na hora de digitar deixa de ser 45.5 para 45,5.
    scanf("%f", &peso);
    printf("\n\n-----------PROCESSANDO----------\n");
    printf("Muito prazer, %s. Você tem %i anos de idade e pesa %.2fKg correto?", nome, idade, peso);  //Aqui continua o ponto %.2f.
    printf("FIM.");
}