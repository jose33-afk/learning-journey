#include <stdio.h>
#include <locale.h>

// <<EX007 - Dobro e Ter�a parte >>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int num, num_dobro;
    float terca_parte;

    printf("Digite um n�mero:");
    scanf("%i", &num);
    num_dobro = num * 2; 
    terca_parte = num / 3.0;  //Para fazer a divisao real, um inteiro e o 3 real, Pode ter alguma divisao que precise do ponto flutuante. terca_parte = (float)num / 3
    printf("Analizando o n�mero %i, seu dobro � %i e sua ter�a parte � %.2f", num, num_dobro, terca_parte);
}
