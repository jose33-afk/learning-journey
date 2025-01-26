#include <stdio.h>
void main() {
    unsigned int idade = 33; //Tipo|nome da variavel|valor||unsigned int idade; sem valor 
    float peso = 87.0;
    char sexo = 'M'; // aspas simples, apenas uma letra
    char *nome = "Juvenal"; // aspas duplas, cadeira de caracteres/string

    printf("%s e do sexo %c e tem %i anos de idade e pesa %.2fKg", nome, sexo, idade, peso);
}