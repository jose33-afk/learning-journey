#include <stdio.h>

int main () {
    int segundos_tecla, horas, minutos, segundos, horas_conver;

    printf("Digite a quantidade de segundos que deseja converter: ");
    scanf("%i", &segundos_tecla);

    //Conversao
    horas = segundos_tecla / 3600; 
    horas_conver = segundos_tecla % 3600; //Auxiliar para conversao nos minutos e segundos.
    minutos = horas_conver / 60;
    segundos = horas_conver - minutos * 60;

    printf("\nConvertendo...\n");
    printf("---------------------\n"
           "Horas: %i\n"
           "Minutos: %i\n"
           "Segundos: %i\n"
           "----------------------", horas, minutos, segundos);
    
    return 0;
}