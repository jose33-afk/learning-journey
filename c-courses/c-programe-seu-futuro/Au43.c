#include <stdio.h>

//Operador ternario.
int main() {

    int a;

    printf("Digite um valor qualquer: ");
    scanf("%i", &a);

    //Parece que é obrigatorio ter duas "verdadeiro" e "falso" ou outra coisa. 2
    a < 0 ? printf("Verdadeiro") : printf("Falso"); //Condiçao|opcao 1| opcao 2 | assim que funciona. 
    
    printf(a > 0? "\nO numero eh positivo" : "O numero eh negativo\n"); //assim funciona tambem, interresante...
 
    return 0;
}