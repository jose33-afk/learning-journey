#include <stdio.h>
#include <string.h>
//como criar novos tipos de dados em c com typedef struc

typedef struct {
    int idade; //variaveis do tipo pessoa.
    char sexo;
    char nome[100];
}Pessoa;   //nome

struct Pessoa2{ //mesma funcao do primeiro
    int idade;
    char sexo;
    char nome[100];
};

int main() {
    //Pessoa /nome da variavel pode ser qualquer um.
    Pessoa pessoa1; //typedef struc //melhor essa 
    //struct Pessoa2 pessoa2; // struct Pessoa2    //variavel do tipo pessoa que eu criei no struct. //
    //char nome[100] = "Maria"; //so funciona na criaçao

    //pessoa2.idade = 33; //se for fazer a declaraçao struct pessoa2 é a mesma coisa, so mudar o nome de pessoa1.idade para pessoa2.idade.
    
    pessoa1.idade = 35; 
    pessoa1.sexo = 'F';
    strcpy(pessoa1.nome, "Jose"); //assim, funciona variavel normal e assim.

    printf("Nome: %s\n", pessoa1.nome);
    printf("Sexo: %c\n", pessoa1.sexo);
    printf("idade: %i\n", pessoa1.idade);
    return 0;
}