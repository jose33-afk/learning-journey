#include <stdio.h>
#include <locale.h>
#include <time.h>
void main() {
    setlocale(LC_ALL, "Portuguese");
    int hora_atual, hora_filme;
    float quan_dinhe;

    //Hora Atual
    time_t t;
    time(&t);
    struct tm *hora;
    hora = localtime(&t);
    hora_atual = hora->tm_hour;

    printf("========================== CINEMA ==========================\n"
           "Digite somente a hora n use minutos! 7, 13 = 7h 13h\n"
           "------------------------------------------------------------\n"
           "Horario:");
    scanf("%i", &hora_filme);

    printf("\n\n================================================\n"
           "HORARIO DO FILME: %ih - PREÇO DO INGRESSO: R$20\n", hora_filme);
    printf("================================================\n"
           "Quanto dinheiro você tem? R$");
    fflush(stdin);
    scanf("%f", &quan_dinhe);
    printf("Agora são %i horas.\n", hora_atual);

    if ((quan_dinhe >= 20) && (hora_atual < hora_filme)){
        printf("Voce consegue comprar o ingresso!");
    } else {
        printf("Infelismente não é possivel comprar o ingresso!");
    }

}
//versao 1.0, a versao 2.0 vai permitir minutos, ainda n cheguei na aula que preciso pra fazer isso.