#import <stdio.h>
void main() {
    char nome[] = "Gustavo guanabara";
    printf("<%30s>", nome);  //Escreve com 30 espaçoes e alinha. %30s alinha pra --> %-30s alinha pra ca <--- Funciona com %c tambem
}

//  printf("%-30s", "Nome"); funciona tambem