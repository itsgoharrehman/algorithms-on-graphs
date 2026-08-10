#python3
import sys
from collections import deque

def is_bipartite(adj, n):
    color = [-1] * (n + 1)

    for start in range(1, n + 1):
        if color[start] == -1:
            color[start] = 0
            queue = deque([start])

            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[curr]
                        queue.append(neighbor)
                    elif color[neighbor] == color[curr]:
                        return 0
    return 1

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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    print(is_bipartite(adj, n))

if __name__ == '__main__':
    main()