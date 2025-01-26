#include <stdio.h>
void main() {
    /*float x = 5;
    int y = 2;
    float z = (float)x / y; // forca a variavel a virar um float ou (int)variavel a ser forcada.
    printf("O resultado e %.1f", z);*/
    int x = 65;
    printf("Eu tenho %.2f", (float)x); // Nao muda o tipo primitivo da variavel, apenas na linha onde foi declarada o type cast.
    printf("\nEu tenho %i", x);
}