import heapq

LIMIT = 100000
MAXN = 10100

def main():
    n, c, s, b = map(int, input().split())
    
    grafo_bino = [[] for _ in range(MAXN)]
    grafo_criminosos = [[] for _ in range(MAXN)]
    distancias_bino = [LIMIT] * MAXN
    distancias_criminosos = [LIMIT] * MAXN
    visitado_bino = [0] * MAXN
    visitado_criminosos = [0] * MAXN
    resposta = 0
    
    for i in range(c):
        u, v, peso = map(int, input().split())
        grafo_bino[u - 1].append((v - 1, peso))
        grafo_bino[v - 1].append((u - 1, peso))
        grafo_criminosos[u - 1].append((v - 1, peso))
        grafo_criminosos[v - 1].append((u - 1, peso))
    
    for i in range(s):
        u, v, peso = map(int, input().split())
        grafo_criminosos[u - 1].append((v - 1, peso))
        grafo_criminosos[v - 1].append((u - 1, peso))
    
    bandidos = list(map(int, input().split()))
    k, f = map(int, input().split())
    
    fila_bino = [(0, f - 1)]
    
    while fila_bino:
        davez = heapq.heappop(fila_bino)
        if visitado_bino[davez[1]]:
            continue
        visitado_bino[davez[1]] = 1
        distancias_bino[davez[1]] = min(distancias_bino[davez[1]], davez[0])
        
        for atual in grafo_bino[davez[1]]:
            if not visitado_bino[atual[0]]:
                heapq.heappush(fila_bino, (atual[1] + davez[0], atual[0]))
    
    fila_criminosos = [(0, f - 1)]
    
    while fila_criminosos:
        davez = heapq.heappop(fila_criminosos)
        if visitado_criminosos[davez[1]]:
            continue
        visitado_criminosos[davez[1]] = 1
        distancias_criminosos[davez[1]] = min(distancias_criminosos[davez[1]], davez[0])
        
        for atual in grafo_criminosos[davez[1]]:
            if not visitado_criminosos[atual[0]]:
                heapq.heappush(fila_criminosos, (atual[1] + davez[0], atual[0]))
    
    tempobino = distancias_bino[k - 1]
    
    for i in range(b):
        if distancias_criminosos[bandidos[i] - 1] <= tempobino:
            resposta += 1
    
    print(resposta)

if __name__ == "__main__":
    main()