#include <stdio.h>
#include <string.h>

// Como criar uma struct com dados lidos do teclado.

typedef struct {
    int idade;
    char sexo;
    char nome[100];
}Pessoa;   



int main() {
    Pessoa pessoa; 
    
    printf("Digite o seu nome: ");
    fgets(pessoa.nome, 100, stdin); //pra ler strings, variavel, tamanho da string, stdin. pra ler do teclado.
    printf("Digite sua idade: ");
    scanf("%i", &pessoa.idade); //Basicamente é como ler uma variavel normal so muda a forma que é escrita.
    
    scanf("%c", &pessoa.sexo);
    printf("Nome: %s\n", pessoa.nome);
    //printf("Sexo: %c\n", pessoa.sexo);
    printf("idade: %i\n", pessoa.idade);
    return 0;
}