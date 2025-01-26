#include <stdio.h>
#include <string.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    char estado[2];

    printf("Em que estado do Brasil voce nasceu? "); 
    gets(estado);
    printf("Nascendo em %s voce e ", estado);

    if (strcmp(estado, "RJ") == 0) {
        printf("CARIOCA!");
    } else if (strcmp(estado, "SP") == 0) {
        printf("PAULISTA!");
    } else if (strcmp(estado, "MG") == 0) {
        printf("MINEIRO!");
    } else if (strcmp(estado, "AL") == 0) {
        printf("ALAGOANO");
    } else if (strcmp(estado, "RN") == 0) {
        printf("POTIGUAR!");
    } else {
        printf("natural da sua cidade, mas ainda não sei como te chamar!");
    }

}