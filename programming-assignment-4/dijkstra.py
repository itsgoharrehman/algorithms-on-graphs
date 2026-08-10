#python3
import sys
import heapq

def dijkstra(adj, s, t, n):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        if u == t:
            return d

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist[t] if dist[t] != float('inf') else -1

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
    t = int(input_data[idx + 1])

    print(dijkstra(adj, s, t, n))

if __name__ == '__main__':
    main()