#include <stdio.h>
#include <stdlib.h> //Bibioteca do system
// system("pause") //Pra Windows

int main () {
    printf("Testes");
    system("pause"); //Pausa o programa até o usuário pressionar uma tecla,  tem que por no final, porq senao ele fecha sem mostrar o resultado, se a pessoa n tiver uma ide no pc
    return 0;
  
 // Seu código
    printf("Pressione Enter para continuar..."); //mesmo efeito do sytem
    getchar();  // Espera o usuário apertar Enter OBS: Tem que por dois getchar();
    return 0;
}
