#include <stdio.h>

// Estrutura de seleçao switch case com caracter:

int main() {

    char opcao;

    printf("Opcoes:\n"
           "a - ola\n"
           "b - hello");
    opcao = getchar();

    switch (opcao) {     
        case 'a':  //lembra, caracter '' e string "".
            printf("Ola!");
            break;
        case 'b':
            printf("Hello!");
        
    }

    return 0;
}

/*Boa pergunta.
//gostei muito do vídeo , já me ajudou , como faço para o computador aceitar tanto maiúsculo quando minúsculo ?

A estrutura switch case não aceita intervalos, apenas uma comparação de igualdade. Assim, se você precisa verificar minúsculo e maiúsculo, serão necessários dois cases, um para cada caracter, assim:

case 'a':
  // codigo do case a
  break;
case 'A':
  // código do case A
  break;

Se o mesmo trecho de código for executado para 'a' e para 'A', você pode fazer uma função ou procedimento e chamá-lo dentro dos dois cases, assim você escreve o trecho de código apenas uma vez.

case 'a':
  minha_funcao();
  break;
case 'A':
  minha_funcao();
  break;
*/

/*

case 'A': //Interresante ja que ele pula pra seguinte sem ter um break
case 'a':
    printf("Mensagem para A ou a\n");
    break;
case 'B':
case 'b':
    printf("Mensagem para B ou b\n");
    break;
*/