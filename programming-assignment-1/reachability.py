#python3
import sys

def is_reachable(adj, u, v):
    visited = [False] * len(adj)
    stack = [u]
    visited[u] = True

    while stack:
        curr = stack.pop()
        if curr == v:
            return 1
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                
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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    u = int(input_data[idx])
    v = int(input_data[idx + 1])

    print(is_reachable(adj, u, v))

if __name__ == '__main__':
    main()