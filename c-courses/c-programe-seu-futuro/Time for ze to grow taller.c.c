#include <stdio.h> 

/*22) Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3
centímetros por ano. Construa um programa que calcule e imprima quantos anos serão necessários
para que Zé seja maior que Chico.*/
 
float calculation (float hei1, float hei2, int centi){  //Don't forget to specify the function's type with the same result it will return. //this "hei1" is bigger
    float cont;

    for (cont=hei2; cont<=hei1; cont+=centi){
        printf("%f", cont);
    }
  
}

int main() {
    float height[2], cent[2], difference;
    
    printf("How long"
           "\n--------------\n");
    printf("Fist person:\n");
    printf("Enter your height in meters:");
    scanf("%f", &height[0]);
    printf("How many centimeters do you grow per year: ");
    scanf("%f", &cent[0]);

    printf("--------------\n"
           "Second person:\n"
           "Enter your height in meters:");
    scanf("%f", &height[1]);
    printf("How many centimeters do you grow per year: ");
    scanf("%f", &cent[1]);

    if (height[0] > height[1]) {
        difference = calculation(height[0], height[1], cent[1]); //this height[0] is bigger
    } else difference = calculation(height[1], height[0], cent[0]); //this height[1] is bigger

    printf("Difference: %.2f", difference);
}

 