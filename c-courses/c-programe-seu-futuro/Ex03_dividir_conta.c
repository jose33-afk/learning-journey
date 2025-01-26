#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    float conta_restaurant, gorjeta;
    int porcent_gjt, quant_pesso;

    printf("Qual foi o valor da conta? R$");
    scanf("%f", &conta_restaurant);
    printf("Quanto porcento de R$%.2f que vai dar de gorjeta? %%", conta_restaurant);
    scanf("%i", &porcent_gjt);
   
    //Valor da gorjeta
    gorjeta = conta_restaurant * porcent_gjt / 100;

    printf("\n\nQuantas pessoas vao dividir a conta?\n"
           "Pessoas:");
    scanf("%i", &quant_pesso);
    printf("========================================\n");
    printf("Valor da gorjeta: R$%.2f.\n", gorjeta);
    printf("----------------------------------------\n");

    gorjeta /= quant_pesso; //Valor por pessoa a pagar.
    
    printf("Valor por pessoa a pagar a gorjeta R$%.2f\n", gorjeta);
    printf("========================================\n");
    
    system("pause");
    return 0;
}