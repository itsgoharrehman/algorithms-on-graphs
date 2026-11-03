<div align="center">
  <h1>algorithms-on-graphs</h1>
  <p>Graph algorithms, shortest paths, spanning trees, and network flow implementations for the UC San Diego course.</p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License"></a>
    <img src="https://img.shields.io/badge/Institution-UC_San_Diego-182B49?style=flat-square&logo=coursera&logoColor=white" alt="UC San Diego">
    <img src="https://img.shields.io/badge/Language-Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Focus-Graph_Theory_&_Algorithms-E34F26?style=flat-square&logo=thealgorithms&logoColor=white" alt="Graph Theory">
    <a href="https://github.com/itsgoharrehman/algorithms-on-graphs/stargazers"><img src="https://img.shields.io/github/stars/itsgoharrehman/algorithms-on-graphs?style=flat-square&logo=github&logoColor=white" alt="Stars"></a>
    <a href="https://github.com/itsgoharrehman/algorithms-on-graphs/issues"><img src="https://img.shields.io/github/issues/itsgoharrehman/algorithms-on-graphs?style=flat-square&logo=github&logoColor=white" alt="Issues"></a>
  </p>
</div>

---

> [!IMPORTANT]
> **Academic Honesty and Institutional Integrity**:
> This repository contains completed algorithmic coursework for the University of California San Diego's **Algorithms on Graphs** course (part of the Computer Science Data Structures & Algorithms Specialization). In accordance with UCSD's Policy on Integrity of Scholarship and the Coursera Honor Code, students currently enrolled in the course are strictly prohibited from copying, plagiarizing, or submitting any part of these solutions. This repository exists solely for code review, pedagogical reference, and portfolio demonstration.

---

## Core Graph Algorithms & Asymptotic Complexity Matrix

The repository implements essential graph theory algorithms satisfying rigorous competitive programming execution constraints:

| Module | Problem / Algorithm | Description & Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Assignment 1** | Path Reachability (`reachability.py`) | DFS traversal between source and target | `O(|V| + |E|)` | `O(|V|)` |
| **Assignment 1** | Connected Components (`connected_components.py`) | Undirected graph component labeling | `O(|V| + |E|)` | `O(|V|)` |
| **Assignment 2** | Acyclicity Check (`acyclicity.py`) | Directed cycle detection via DFS recursion stack | `O(|V| + |E|)` | `O(|V|)` |
| **Assignment 2** | Topological Sort (`toposort.py`) | Reverse post-visit order DFS on DAG | `O(|V| + |E|)` | `O(|V|)` |
| **Assignment 2** | Strongly Connected (`strongly_connected.py`) | Kosaraju's two-pass DFS on transposed graph | `O(|V| + |E|)` | `O(|V| + |E|)` |
| **Assignment 3** | Breadth-First Search (`bfs.py`) | Unweighted single-source shortest path | `O(|V| + |E|)` | `O(|V|)` |
| **Assignment 3** | Bipartite Verification (`bipartite.py`) | 2-coloring graph partition via BFS | `O(|V| + |E|)` | `O(|V|)` |
| **Assignment 4** | Dijkstra's Algorithm (`dijkstra.py`) | Non-negative edge shortest path with min-heap | `O((|V| + |E|) log |V|)` | `O(|V| + |E|)` |
| **Assignment 4** | Negative Cycle Detection (`negative_cycle.py`) | Bellman-Ford algorithm (|V|-th edge relaxation) | `O(|V| * |E|)` | `O(|V|)` |
| **Assignment 4** | Arbitrage Shortest Paths (`shortest_paths.py`) | Multi-phase Bellman-Ford with BFS reachability | `O(|V| * |E|)` | `O(|V|)` |
| **Assignment 5** | Minimum Spanning Tree (`connecting_points.py`) | Kruskal's algorithm with Disjoint Sets | `O(|E| log |V|)` | `O(|V| + |E|)` |
| **Assignment 5** | Optimal Clustering (`clustering.py`) | Kruskal-based maximum spacing k-clustering | `O(|E| log |V|)` | `O(|V| + |E|)` |

---

## Directory Structure

```
algorithms-on-graphs/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml              # Defect reporting form
│   │   └── question.yml                # Conceptual graph question form
│   ├── PULL_REQUEST_TEMPLATE.md        # Academic integrity verification checklist
│   └── dependabot.yml                  # Weekly automated pip dependency scanner
├── programming-assignment-1/           # Decomposition of graphs (DFS, connected components)
├── programming-assignment-2/           # Paths in directed graphs (topological sort, SCC)
├── programming-assignment-3/           # Paths in graphs (BFS, bipartite graph testing)
├── programming-assignment-4/           # Paths with weights (Dijkstra, Bellman-Ford, negative cycles)
├── programming-assignment-5/           # Minimum spanning trees (Kruskal, optimal clustering)
├── requirements.txt                    # Testing dependencies
├── LICENSE                             # MIT License
├── SECURITY.md                         # Security policy and disclosure protocol
├── CONTRIBUTING.md                     # Academic archive contribution guidelines
└── CODE_OF_CONDUCT.md                 # Contributor Covenant v2.1
```

---

## Running and Testing Locally

### Prerequisites

* Python 3.10 or higher
* `pytest` for automated test execution

### Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/itsgoharrehman/algorithms-on-graphs.git
   cd algorithms-on-graphs
   ```

2. Install test dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run an algorithm script against input fixtures:
   ```bash
   python programming-assignment-2/toposort.py
   python programming-assignment-4/dijkstra.py
   python programming-assignment-5/connecting_points.py
   ```

---

## Academic Governance and Licensing

* **License**: Licensed under the terms of the [MIT License](LICENSE).
* **Security Policy**: See [SECURITY.md](SECURITY.md) for vulnerability disclosure.
* **Academic Guidelines**: See [CONTRIBUTING.md](CONTRIBUTING.md) regarding preservation of completed coursework.
