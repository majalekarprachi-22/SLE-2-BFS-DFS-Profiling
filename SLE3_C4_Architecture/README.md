# SLE-3: Architectural Design (Full C4 Model)

## Course
02AML204 – Introduction to Artificial Intelligence

## System Title
Graph Search System Using BFS and DFS

## Student Details
- Name: Prachi Majalekar
- PRN: 25UAM118
- Division: B

## System Overview

This project presents the architectural design of a Graph Search System using
Breadth-First Search (BFS) and Depth-First Search (DFS).

The system works on a 26-node graph containing nodes from A to Z.
BFS explores nodes level by level using a queue, while DFS explores nodes
depth-wise using a stack.

The SLE-3 architecture is designed using the C4 Model with four levels:
Context, Container, Component, and Code Level.

This SLE-3 is a continuation of the BFS and DFS system used in SLE-2.

---

## 1. Context Diagram

The Context Diagram shows the interaction between the user and the
Graph Search System.

The user provides the start and goal node.
The system performs BFS or DFS and provides the search result.

Diagram file:

`01_Context_Diagram.drawio`

---

## 2. Container Diagram

The Container Diagram shows the main parts of the system:

- Input Module
- Graph Management
- Search Engine
- Visited / Memory
- Output Module

Graph Management stores the 26-node A–Z graph.
The Search Engine performs BFS and DFS.
Visited / Memory stores visited nodes.
The Output Module provides the search result.

Diagram file:

`02_Container_Diagram.drawio`

---

## 3. Component Diagram

The Component Diagram shows the internal structure of the Search Engine.

The main components are:

- BFS Queue
- DFS Stack
- Goal Test
- Visited Set

BFS uses a queue following FIFO, while DFS uses a stack following LIFO.
The Goal Test checks whether the current node is the goal node.

Diagram file:

`03_Component_Diagram.drawio`

---

## 4. Code Level Overview

The Code Level shows the main code elements used in the BFS and DFS
implementation:

- `graph` – stores the A–Z adjacency list
- `bfs()` – performs BFS using a queue
- `dfs()` – performs DFS using a stack
- `visited` – stores visited nodes
- `nodes_explored` – counts explored nodes

Benchmark and profiling files were also used in SLE-2 for performance
analysis.

Diagram file:

`04_Code_Level_Diagram.drawio`

---

## 5. Design Decisions

- BFS uses a queue for level-wise exploration.
- DFS uses a stack for depth-wise exploration.
- A visited set avoids repeated exploration.
- The graph representation is kept separate from BFS and DFS functions.
- The same system is continued from SLE-2 for architectural design.

---

## 6. AI Contribution

AI tools were used for guidance in understanding the C4 architecture,
organizing the diagrams, explaining design decisions, and preparing the
documentation.

The implementation, diagrams, project structure, and final design decisions
were reviewed and prepared by the student.

---

## 7. Project Files

```text
SLE3_C4_Architecture
│
├── 01_Context_Diagram.drawio
├── 02_Container_Diagram.drawio
├── 03_Component_Diagram.drawio
├── 04_Code_Level_Diagram.drawio
└── README.md

## 8. Relation with SLE-2

SLE-3 is a continuation of the BFS and DFS system developed in SLE-2.

SLE-2 focused on performance analysis, while SLE-3 defines the complete
system architecture using the C4 Model.

This connects the implementation, performance analysis, and architecture
of the same Graph Search System.

---

## Conclusion

The C4 model provides a clear view of the Graph Search System at different
levels.

The four diagrams explain the system structure, components, and main code
elements of BFS and DFS.