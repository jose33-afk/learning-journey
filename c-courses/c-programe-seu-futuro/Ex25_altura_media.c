#include <stdio.h>
#include <locale.h>

/*Para uma turma de 45 alunos, construa um algoritmo que determine:
a) A idade média dos alunos com menos de 1,70m de altura;
b) A altura média dos alunos com mais de 20 anos.
*/

int main() {
    setlocale(LC_ALL, "Portuguese");
    float altura, altura_med20 = 0;
    int idade, idade_media = 0, i, menor_tf = 0, altu_f = 0;
    	
    for (i=1; i<3;  i++) {
        printf("Qual a idade do %iº aluno:", i);
        scanf("%i", &idade);
        printf("Agora a altura: ");
        scanf("%f", &altura);
        printf("\n");

        if (altura < 1.70) {
            idade_media += idade;
            menor_tf++;
        }
        if (idade > 20) {
            altura_med20 += altura;
            altu_f++;
        }
        
    }

    //idade 1,70m
    if (menor_tf >= 2) printf("A idade media de alunos com menos de 1,70m\nMédia:%.2f", idade_media / 2.0);
    else if (altu_f == 1) printf("\nNão é possivel fazer o calculo!! com somente um valor..");
    else printf("Nenhuma pessoa com 1,70m foi cadastrada!");

    //altura 20+ anos
    if (altu_f >= 2) printf("\nE altura média dos al=unos com mais de 20 anos.\nMédia:%.2f", altura_med20 / 2.0);
    else if (altu_f == 1) printf("\nNão é possivel fazer o calculo!! com somente um valor..");
    else printf("\nNenhuma pessoa com mais de 20 anos foi encontrada!\n");

    printf("\nPressione Enter para fechar...");
    getchar();
    getchar();

    return 0;
}