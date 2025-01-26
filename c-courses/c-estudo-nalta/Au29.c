#include <stdio.h>
#include <time.h> 
// Data e hora sistema.

void main() {
    time_t t;  //Vai receber a data atual
    time(&t);   //Ativaçao da variavel t

    struct tm * data; //Criaçao da strutura "Tm=nome_da_variavel" e ponteiro data=nome_da_variavel || * é poteiro e n multiplicaçao aqui.
    data = localtime(&t); //Pelo que eu entendi, uma struct é um block separado, que comporta funçoes mas n pode ser acessado diretamente,
                          // por isso precisa de um intermediario no caso uma variavel, que nesse caso é a "data".
    
    int d = data->tm_mday; //dia atual    
    int mes = data->tm_mon + 1; // Tem que por mais 1, porque o mes de janeiro é considerado mes 0.
    int ano = data->tm_year + 1900; // tem que por Obs:so nessa biclioteca + 1900

    printf("Estamos no dia %i do mes %i e no ano de %i", d, mes, ano);

}
/*time_t nome_variavel;
time(&t);   anotaçao, sempre que o & esta em frente a uma variave, eu estou passando o endereço dela para um determinada funcao ou funcionalidade.

/* - ponteiro
struct nome_struct*data;  
data = localtime(&t);
*/

//int d = data->tm_mday; basicamente a variavel "D" recebe o dia|| data ta apontando para a struct e pegando a funçao especifica de localtime, que é a tm_mday;

/*struct tm {
    int tm_sec;    // segundos (0-60)
    int tm_min;    // minutos (0-59)
    int tm_hour;   // horas (0-23)
    int tm_mday;   // dia do mês (1-31)
    int tm_mon;    // mês (0-11, onde 0 = janeiro)
    int tm_year;   // anos desde 1900
    int tm_wday;   // dia da semana (0-6, onde 0 = domingo)
    int tm_yday;   // dia do ano (0-365)
    int tm_isdst;  // horário de verão (-1, 0, 1)
};
*/
