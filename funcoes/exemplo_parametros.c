#include <stdio.h>

int contagem_regressiva(int num) {
    while (num > 0) {
        num = num - 1;
    }
    return num;
}

int contagem_regressiva_referencia(int *num) {
    while (*num > 0) {
        *num = *num - 1;
    }
    return *num;
}

int main() {
    int a = 100;
    int resp = contagem_regressiva(a);
    printf("%d, %d\n", resp, a);

    resp = contagem_regressiva_referencia(&a);
    printf("%d, %d\n", resp, a);

    return 0;
}