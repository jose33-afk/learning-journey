#include <stdio.h>

/*
    tamanho de um float na memoria 
    tipo double 
    %lf
    long double -> %Lf mas so funcona no linux e mac. 
    pra imprimir no windos __mingw_printf();
*/

int main () {
    
    float x = 3.1415; // nao da pra short float e long float, so no int, da erro. //precisao simples 

    double y = 3.1324343453546464646;
    long double a;

    printf("Um long duble precisa de %i bytes de memoria:\n", sizeof a);	
    printf("Um double precisa de %i bytes de memoria. \n", sizeof y);
    printf("Um float precisa de %i bytes de memoria. \n", sizeof x);
    __mingw_printf("Valor de y: %lf", y);
    //printf("Valor de y %.10lf", y); //tanto o float quanto o double, so imprime 6 digitos apos o . por padrao, pra mostrar mais so formatar

    return 0;
}