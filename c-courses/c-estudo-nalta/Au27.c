#include <stdio.h>

/*Operadores bitwise
>> - right shift
<< - left shift
*/
void main() {
    int n = 43 >> 3; // bits normal|quantidade de bits a mais para <-- 
    //int n2 19 >> 2; //Mesma coisa do <<, so que aqui perde dois bits para -->
    printf("O resultado foi %i", n);
}