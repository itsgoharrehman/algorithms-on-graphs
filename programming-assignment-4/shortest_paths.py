#python3
import sys
from collections import deque

def shortest_paths(adj, s, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    reachable = [False] * (n + 1)
    shortest = [True] * (n + 1)

    dist[s] = 0
    reachable[s] = True

    # 1. Bellman-Ford for n-1 iterations
    for _ in range(n - 1):
        for u in range(1, n + 1):
            if dist[u] != INF:
                for v, w in adj[u]:
                    reachable[v] = True
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

    # 2. Collect nodes affected by negative cycles on n-th iteration
    queue = deque()
    for u in range(1, n + 1):
        if dist[u] != INF:
            for v, w in adj[u]:
                reachable[v] = True
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    queue.append(v)

    # 3. BFS to mark all nodes reachable from negative cycles
    visited = [False] * (n + 1)
    while queue:
        u = queue.popleft()
        if not visited[u]:
            visited[u] = True
            shortest[u] = False
            for v, w in adj[u]:
                queue.append(v)

    return dist, reachable, shortest

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n + 1)]
    idx = 2

    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        adj[u].append((v, w))
        idx += 3

    s = int(input_data[idx])

    dist, reachable, shortest = shortest_paths(adj, s, n)

    for i in range(1, n + 1):
        if not reachable[i]:
            print('*')
        elif not shortest[i]:
            print('-')
        else:
            print(dist[i])

if __name__ == '__main__':
    main()