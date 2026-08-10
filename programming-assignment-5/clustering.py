#python3
import sys
import math

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            return True
        return False

def clustering(x, y, k, n):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.hypot(x[i] - x[j], y[i] - y[j])
            edges.append((dist, i, j))

    edges.sort(key=lambda item: item[0])

    dsu = DisjointSet(n)
    num_clusters = n

    for dist, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            if num_clusters == k:
                return dist
            dsu.union(u, v)
            num_clusters -= 1

    return 0.0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    x = []
    y = []
    idx = 1
    for _ in range(n):
        x.append(int(input_data[idx]))
        y.append(int(input_data[idx + 1]))
        idx += 2

    k = int(input_data[idx])

    print(f"{clustering(x, y, k, n):.9f}")

if __name__ == '__main__':
    main()