#python3
import sys

def has_negative_cycle(adj, n):
    dist = [0] * (n + 1)

    for _ in range(n - 1):
        relaxed = False
        for u in range(1, n + 1):
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    relaxed = True
        if not relaxed:
            return 0

    # N-th iteration to check for negative cycles
    for u in range(1, n + 1):
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                return 1

    return 0

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

    print(has_negative_cycle(adj, n))

if __name__ == '__main__':
    main()