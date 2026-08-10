#python3
import sys

sys.setrecursionlimit(200000)

def dfs_order(node, adj_rev, visited, order):
    visited[node] = True
    for neighbor in adj_rev[node]:
        if not visited[neighbor]:
            dfs_order(neighbor, adj_rev, visited, order)
    order.append(node)

def dfs_scc(node, adj, visited):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs_scc(neighbor, adj, visited)

def number_of_sccs(adj, adj_rev, n):
    visited = [False] * (n + 1)
    order = []

    # Step 1: DFS on reversed graph G^R to get post-order
    for i in range(1, n + 1):
        if not visited[i]:
            dfs_order(i, adj_rev, visited, order)

    # Step 2: DFS on original graph G in reverse post-order
    visited = [False] * (n + 1)
    scc_count = 0

    while order:
        node = order.pop()
        if not visited[node]:
            dfs_scc(node, adj, visited)
            scc_count += 1

    return scc_count

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n + 1)]
    adj_rev = [[] for _ in range(n + 1)]
    idx = 2

    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj_rev[v].append(u)
        idx += 2

    print(number_of_sccs(adj, adj_rev, n))

if __name__ == '__main__':
    main()