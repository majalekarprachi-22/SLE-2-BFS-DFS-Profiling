# SLE-2: BFS vs DFS Profiling

## Course
02AML204 – Introduction to Artificial Intelligence

## Student Details
- Name: Prachi Majalekar
- PRN: 25UAM118
- Program: SY B.Tech CSE (AI & ML)

---

## Problem Statement

To implement BFS and DFS search algorithms on the same graph and compare their practical performance using execution time and number of nodes explored.

---

## Algorithms Used

### 1. Breadth First Search (BFS)
BFS explores the graph level by level using a queue.

### 2. Depth First Search (DFS)
DFS explores the graph by going as deep as possible before backtracking using a stack.

---

## Graph Used

A 26-node graph using nodes A to Z was used for the experiment.

- Start Node: A
- Goal Node: Z

Both BFS and DFS were tested on the same graph and with the same start and goal nodes.

---

## Profiling Method

The performance was measured using:

- Python `time.perf_counter()` for execution time.
- Execution time was converted into milliseconds (ms).
- Number of nodes explored was counted during the search.
- Three separate runs were performed for BFS and DFS.
- `py-spy` version 0.4.2 was also used for profiling.
- The profiling output was saved as `profile.svg`.

---

## Performance Results

| Algorithm | Nodes Explored | Best Time (ms) | Average Time (ms) | Worst Time (ms) |
|-----------|----------------|----------------|-------------------|-----------------|
| BFS       | 26             | 0.010200       | 0.011267          | 0.012900        |
| DFS       | 25             | 0.009500       | 0.010600          | 0.011400        |

---

## Analysis

- BFS explored 26 nodes to reach the goal node Z.
- DFS explored 25 nodes to reach the same goal.
- In the three measured runs, DFS had a slightly lower average execution time than BFS.
- The execution time varied slightly between different runs.
- The number of nodes explored depends on the graph structure and traversal order.
- BFS uses a queue, while DFS uses a stack, which affects their traversal behaviour.
- The experiment shows that practical performance can differ from theoretical complexity depending on the input graph and implementation.

---

## Py-spy Profiling

Py-spy was used to observe the execution behaviour of BFS and DFS.

The profiling session included:

- Best Case: Goal node B
- Average Case: Goal node J
- Worst Case: Goal node Z

The profiling result was saved as:

`profile.svg`

---

## AI Contribution Note

AI tools were used to understand the SLE-2 requirements, get guidance for implementing BFS and DFS, understand performance measurement, and get guidance for using py-spy.

The code was executed and tested by the student. The execution-time results and node counts were obtained from the student's own runs.

---

## Conclusion

BFS and DFS were successfully implemented and profiled on the same 26-node graph. The experiment measured execution time and nodes explored using actual program runs. The results show that traversal order, graph structure, and implementation can affect practical performance. Py-spy was also used to obtain profiling evidence for the experiment.