#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    printf(" %s tem %i anos de idade\n", "Jose Carlos", 18); //%s para caideia de caractere ""||||%i para int
    printf("Seu peso atual e de %6.2fKg\n", 87.0); //%f float/double
    printf("Seu sexo e %c", 'M'); //%c para uma letra ''
}