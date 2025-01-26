#include <stdio.h>
/*Leia numeros
N tem nenhum problema usar o scanf pra numeros, só da problema com caracters.
o scanf so é recomendado pra ler numeros.*/
void main() {
    int n;
    float m; 
    printf("Digite um numero inteiro:");
    scanf("%i", &n);  //Não pode escrever no lugar da formataçao.
    printf("Digite um numero real:");  //Dá para digitar um numero interio, que ele transforma em real
    scanf("%f", &m);  //& obrigatorio
    printf("Voce acabou de digitar os valores %i e %.2f. Obrigado!", n, m); //Só por o & no scanf
}
