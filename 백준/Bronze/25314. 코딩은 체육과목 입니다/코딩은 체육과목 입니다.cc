#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 0;
    scanf("%d", &a);
    int b = a / 4 - 1;
    for (int i = 0; i < a/4; i++){
        printf("long ");
        if (i == a / 4 - 1){
            printf("int");
        }
    }
    return 0;
}