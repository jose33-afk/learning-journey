#include <stdio.h>
#include <string.h>
void main() {
    /*
    //strcpy() //Ã© para adiconar coisas na variaveis strings
    char sit[10];
    float media = 6.6;
    //Errado sit = (media>=7)?"Aprovado":"reprovado"
    strcpy(sit, (media>=7)?"Aprovado":"Reprovado");   //certo[strcpy(nome, "Gustavo");]   || errado(nome = "Gustavo";)
    printf("%s", sit);*/
    
    /*
    //strlen() len comprimento
    char nome[] = "Gustavo";
    int tam = strlen(nome);   //mesma funcao do len em Python.
    printf("O nome %s tem %i letras", nome, tam);*/

    /*
    //strcpm() 
    char s1[] = "Gustavo";
    char s2[] = "Guanabara";
    int res = strcmp(s1, s2);  //strcmp pra saber se duas strings sao iguais. se der zero sao iguais, senao se uma for maior que a outra vai dar um numero negativo ou positivo.
    printf("O resultado da comparacao e %i", res);*/

    /*
    //strcat() pra juntar duas strings.
    char s1[] = "Gustavo";
    char s2[] = "Guanabara";
    printf("%s", strcat(s1, s2));*/

    //strupr() todas as letras maiusculas.
    //strlwr() todas as letras em minusculas, Obs ele muda a string original.
    char nome[] = "Gustavo";
    printf("%s", strupr(nome));
    printf("%s", strlwr(nome));
}

/* nao tem nenhum problema em adiconar string na declaraçao
char nome[10] = "Jose";

mas tem problema pra por depois ent tem que declarar assim\

strcpy(nome, "Jose");
*/