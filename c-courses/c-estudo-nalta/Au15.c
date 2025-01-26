#include <stdio.h>
#import <stdlib.h>
#import <time.h>
void main() {
    srand(time(NULL));  //Gerar um numero aleatorio 
    int n = rand() % 10 + 1;  //Gera um número aleatório de 1 a 10
    printf("%i", n);  

}