#include <stdio.h>
#include <locale.h>
/*
Escreva um programa que leia o peso e a altura de uma pessoa, 
calcule e mostre o IMC e a faixa em que o indivíduo se enquadra de cordo
*/
int main () {
    setlocale(LC_ALL, "Portuguese");
    float altura, peso, imc;

    printf("CALCULARA IMC\n"
           "-----------------\n");
    
    printf("Qual sua altura (m)? ");
    scanf("%f", &altura);
    printf("Qual seu peso (Kg)? ");
    scanf("%f", &peso);

    //calculo 
    imc = peso / (altura*altura); 

    printf("\nSeu IMC é:%.2f\n", imc);
    printf("----------------------------\n");

    //categoria IMC.
    if (imc < 18.5) printf(" Abaixo do peso!");  //Assim tem o mesmo efeito de por varios if, sem else. ou seja ele executa dois.
    if (imc > 18.5 && imc <= 24.9) printf(" Peso normal");
    if (imc >= 25 && imc <= 29.9) printf(" Sobrepeso");
    if (imc >= 30 && imc <= 34.9) printf(" Obesidade grau 1");
    if (imc >= 35 && imc <= 39.9) printf(" Obesidade grau 2");
    if (imc >= 40) printf(" Obesidade grau 3");

    printf("\n----------------------------\n");
    printf("\nPressione Enter para continuar...");
    getchar();
    getchar();

    return 0;
}