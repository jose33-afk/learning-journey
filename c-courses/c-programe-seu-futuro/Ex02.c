#include <stdio.h>

int main() {
    int a, b;

    printf("Digite o valor da variavel A: ");
    scanf("%i", &a);
    printf("Digite o valor da variavel B: ");
    scanf("%i", &b);
    printf("\nA era originalmente %i.\n"
           "B era originalmente %i.\n", a, b);   
    
    a = b;
    b = a;

    printf("\nA agora contem o valor: %i.\n", a);
    printf("B agora contem o valor: %i.", b);
 

    return 0;
}