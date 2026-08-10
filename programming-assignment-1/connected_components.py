#python3
import sys

def number_of_components(adj, n):
    visited = [False] * (n + 1)
    components = 0

    for i in range(1, n + 1):
        if not visited[i]:
            components += 1
            # Explore the current connected component using iterative DFS
            stack = [i]
            visited[i] = True
            while stack:
                curr = stack.pop()
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

    return components

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

    print(number_of_components(adj, n))

if __name__ == '__main__':
    main()