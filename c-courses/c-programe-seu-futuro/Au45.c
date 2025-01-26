#include <stdio.h>

//Operador ternario alinhado

int main() {
    int a;

    printf("Digite um valor: ");
    scanf("%i", &a);

    a < 0 ? printf("valor negativo!") :
        a > 0 ? printf("Postivo") : printf(""); //Desse jeito ainda precisa que o ultimo tenha duas opcoes.
    
    return 0;
}

//Nota:Olá! Com relação aos ternários, posso aninhar várias a depender da minha condição? Tipo: colocar inúmeras linhas de aninhamento?
//
//minha recomendação é que não faça. Ternários aninhados dificulta muito a compreensão do código.  
//O operador ternário foi criado para substituir em apenas uma linha um if / else simples.