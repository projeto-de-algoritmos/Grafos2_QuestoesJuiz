MAXN = 110
LIMIT = 10000

def main():
    instancia = 1
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        print("Instancia", instancia)
        instancia += 1
        
        matriz = [[LIMIT for _ in range(n + 1)] for _ in range(n + 1)]
        
        for _ in range(m):
            u, v, peso = map(int, input().split())
            matriz[u][v] = matriz[v][u] = min(peso, matriz[u][v])
        
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    matriz[i][j] = min(matriz[i][j], max(matriz[i][k], matriz[k][j]))
        
        for i in range(n + 1):
            matriz[i][i] = 0
        
        q = int(input())
        for _ in range(q):
            origem, destino = map(int, input().split())
            print(matriz[origem][destino])
        
        print()

if __name__ == "__main__":
    main()