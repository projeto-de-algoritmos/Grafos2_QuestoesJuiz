import heapq

MAXN = 101
MAXK = 11
INF = 1e7

grafo = [[] for _ in range(MAXN)]
processado = [[-1] * MAXK for _ in range(MAXN)]

def dijkstra():
    Dijkstra = []
    heapq.heappush(Dijkstra, (0, k, 0, a + b))

    while Dijkstra:
        percorrido, restam, ainda, v = heapq.heappop(Dijkstra)
        if v >= a + 1:
            ainda = 0

        if v == 1:
            print(percorrido)
            break

        if processado[v][restam] >= ainda:
            continue

        processado[v][restam] = ainda

        for i in range(len(grafo[v])):
            u, peso = grafo[v][i]
            if peso <= ainda:
                heapq.heappush(Dijkstra, (percorrido, restam, ainda - peso, u))
            if peso <= l and restam >= 1:
                heapq.heappush(Dijkstra, (percorrido, restam - 1, l - peso, u))
            heapq.heappush(Dijkstra, (percorrido + peso, restam, 0, u))

TC = int(input())
for _ in range(TC):
    a, b, m, l, k = map(int, input().split())

    for i in range(1, a + b + 1):
        grafo[i] = []
        processado[i] = [-1] * (k + 1)

    for _ in range(m):
        u, v, peso = map(int, input().split())
        grafo[u].append((v, peso))
        grafo[v].append((u, peso))

    dijkstra()