#include <stdio.h>
#include <stdlib.h>

int main() {
    short int N, *X, *Y, *R, C, *A1, *A2;
    
    scanf("%ld", &N);
    
    X = malloc(N * sizeof(short int)) //Antena i possui coordenadas X[i].Y[i] e range R[i]
    Y = malloc(N * sizeof(short int))
    R = malloc(N * sizeof(short int))
    
    for (int i=0; i<N; i++)
        scanf("%ld %ld %ld", &X[i], &Y[i], &R[i]);
        
    for (int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if (i!=j) { //evita testar se uma antena alcanca ela propria
                int diferencaX = X[i]-X[j];
                if (diferencaX<0) diferencaX*(-1); //simplificar isso com math.h ou macro
                int diferencaY = Y[i]-Y[j];
                if (diferencaY<0) diferencaY*(-1);
                if (diferencaX <= R[i] && diferencaY <= R[i] {
                    // se entrar aqui entao existe aresta de i pra j.
                }
            }
        }
    }
    
    /*
    scanf("%ld", &C)
    for (int i=0; i<N; i++)
        scanf("%ld %ld", &A1[i], &A2[i]);
    */  
    
    return 0;
}
