#include <stdio.h>
#include <locale.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    printf("\\a\t=\tBeep\n\\n");
    printf("\t=\tNovaLinha\n");
    printf("\\\\\t=\tBarra\n");
    printf("%%%%\t=\tPorcentagem\n");
    printf("\\?\t=\tInterrogaçao\n");    
    printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=");
}