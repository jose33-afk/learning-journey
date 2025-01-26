#include <stdio.h>
void main() {
    int n1, n2;
    printf("Primeiro valor: ");
    fflush(stdin);
    scanf("%i", &n1);
    printf("Segundo valor: ");
    fflush(stdin);
    scanf("%i", &n2);

    if (n1>n2) {
        printf("o maior valor e %i.", n1);  
    } else if (n1<n2) {
            printf("O maior valor e %i", n2);
        } else if (n1==n2) {
                printf("os valores sao iguais")
        }
}

/*  if (n1>n2) printf("o maior valor e %i.", n1);  //da pra simplificar assim, mais so se tiver somente um comando 
    else if (n1<n2) printf("O maior valor e %i", n2);
    else if (n1==n2)printf("os valores sao iguais");
    */