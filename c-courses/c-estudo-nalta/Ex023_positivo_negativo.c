#include <stdio.h>
void main() {
    int num;
    
    printf("Me diga um numero e eu te direi se\n"
           "ele e POSITIVO, NEGATIVO ou NULO\n\n"
           "Digite um numero: ");
    scanf("%i", &num);

    if (num>0) printf("O valor %i digitado e POSITIVO.", num);
    else if (num<0) printf("O valor %i digitado e NEGATIVO.", num);
    else printf("O valor %i e NULO.", num);
}