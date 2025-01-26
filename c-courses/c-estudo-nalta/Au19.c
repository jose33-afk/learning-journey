#include <stdio.h>

//Operador Ternario.
void main() {
    /*
    int a = 4, b = 8;  //Da pra declarar assim.
    //int c = (a>b)?1:2;  //primerio se for verdadeiro/segundo se for falso.
    int c = (a>b)?b*2:a+5;  //()condicao ||| 1:2 o que vai acontecer de acordo com as condiçao que esta entre ().
    printf("O resultado e %i", c);*/


    //float media = 5.5;
    //Nao funciona assim 
    //char sit[20];
    //sit = (media>=7)?"Aprovado":"reprovado";  //Obs o operador "?" so funciona para duas || ?"Aprovado":"reprovado"; || n suporta tres.
    //printf("%s", (media>=7)?"Aprovado":"reprovado");   //Assim funciona.

    int num1, num2, maior;
    printf("Digite um numero: ");
    scanf("%i", &num1);
    printf("Digite outro numero: ");
    scanf("%i", &num2);
    maior = (num1 > num2)?num1:num2;
    printf("O maior numero e %i ", maior);
}