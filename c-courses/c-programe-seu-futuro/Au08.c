#include <stdio.h>
int main() {
    char letra;
    
    printf("Digite uma letra: ");
    letra = getc(stdin); //Le um caracter || stdin entrada padrao/teclado
    printf("Caracter  lido: %c", letra); //gect, ele so pega a primeira letra ou caractrer digitado, se digitar mais de um, isso parece util.
    return 0;
}