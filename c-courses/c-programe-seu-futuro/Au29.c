#include <stdio.h>

/*
    operador unsigned 
    %u
    limite para o tipo int: 2.147.483.647
    shorty int -> %d ou %hi
*/
int main() {

    unsigned int y = 2147483647; // unsigned, somente numeros positivo. numero maximo agr com unsined 4.294.967.295.
    
    unsigned short int y = 55000; // Da pra usar assim agr é uma variavel short int que so tem numeros inteiros positivos.

    printf("\n\t\"%u\"\n\n", ++y);  //lembrete ++y soma antes do print, y++ soma depois.
    printf("unsigned short int: %i", y);
    return 0;
}

// o unsegned tira o bit que seria o do sinal positivo e negativo, assim conseguindo armazerar mais numeros positivos.