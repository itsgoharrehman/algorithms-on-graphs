#python3
import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(200000)

def dfs(node, adj, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in adj[node]:
        if not visited[neighbor]:
            if dfs(neighbor, adj, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    return False

def acyclic(adj, n):
    visited = [False] * (n + 1)
    rec_stack = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i, adj, visited, rec_stack):
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
        adj[u].append(v)
        idx += 2

    print(acyclic(adj, n))

if __name__ == '__main__':
    main()