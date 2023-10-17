#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int origem;
    int destino;
    int peso;
} aresta;

int compara(const void *a, const void *b) {
    aresta *arestaA = (aresta *)a;
    aresta *arestaB = (aresta *)b;
    return arestaA->peso - arestaB->peso;
}

int checa_ciclo(int p[], int origem, int destino) {
    while (p[origem] > -1) {
        origem = p[origem];
    }
    while (p[destino] > -1) {
        destino = p[destino];
    }
    if (origem != destino) {
        p[destino] = origem;
        return 1;
    }
    return 0;
}

int main() {
    int m, n;
    int p[200000];
    aresta arestas[200000];

    while (1) {
        scanf("%d %d", &m, &n);
        if (m == 0 && n == 0) {
            return 0;
        }

        int custo = 0, custoTotal = 0;

        for (int i = 0; i < m; i++) {
            p[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            scanf("%d %d %d", &arestas[i].origem, &arestas[i].destino, &arestas[i].peso);
            custoTotal += arestas[i].peso;
        }

        qsort(arestas, n, sizeof(aresta), compara);

        int i = 0;
        int j = 1;

        while (j < m && i < n) {
            if (checa_ciclo(p, arestas[i].origem, arestas[i].destino)) {
                j++;
                custo = custo + arestas[i].peso;
            }
            i++;
        }

        printf("%d\n", custoTotal - custo);
    }

    return 0;
}
