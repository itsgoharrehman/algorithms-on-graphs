#python3
import sys
from collections import deque

def distance(adj, u, v, n):
    dist = [-1] * (n + 1)
    dist[u] = 0
    queue = deque([u])

    while queue:
        curr = queue.popleft()
        if curr == v:
            return dist[v]
        for neighbor in adj[curr]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr] + 1
                queue.append(neighbor)

    return dist[v]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n + 1)]
    idx = 2

    for _ in range(m):
        u_node = int(input_data[idx])
        v_node = int(input_data[idx + 1])
        adj[u_node].append(v_node)
        adj[v_node].append(u_node)
        idx += 2

    u = int(input_data[idx])
    v = int(input_data[idx + 1])

    print(distance(adj, u, v, n))

if __name__ == '__main__':
    main()