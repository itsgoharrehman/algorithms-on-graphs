#python3
import sys

sys.setrecursionlimit(200000)

def dfs(node, adj, visited, order):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, order)
    order.append(node)

def toposort(adj, n):
    visited = [False] * (n + 1)
    order = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, adj, visited, order)

    return order[::-1]

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
        idx += 2

    order = toposort(adj, n)
    print(" ".join(map(str, order)))

if __name__ == '__main__':
    main()