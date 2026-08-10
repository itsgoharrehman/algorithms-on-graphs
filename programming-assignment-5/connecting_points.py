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

def minimum_distance(x, y, n):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.hypot(x[i] - x[j], y[i] - y[j])
            edges.append((dist, i, j))

    edges.sort(key=lambda item: item[0])

    dsu = DisjointSet(n)
    total_weight = 0.0
    edges_count = 0

    for dist, u, v in edges:
        if dsu.union(u, v):
            total_weight += dist
            edges_count += 1
            if edges_count == n - 1:
                break

    return total_weight

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

    print(f"{minimum_distance(x, y, n):.9f}")

if __name__ == '__main__':
    main()