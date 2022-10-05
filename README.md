# Depth-first search

## Purpose

The coding exercises are designed to test knowledge of the following concepts:

* The depth-first search traversal
* Applying the depth-first search traversal in practice

## Overview

The coding exercises cover the following practical problems:
* Checking if a (v, u)-path exist in a directed graph
* Checking if an undirected connected graph is bipartite
* Finding the length of the longest eligible path in a directed acyclic graph

## Coding exercises

### Exercise 1: Check if a (v, u)-path exist in a directed graph

Given the number of vertices `n`, graph edges (adjacency dictionary) `edges` and vertices `v` and `u` for a directed graph, implement the function below to check whether (v, u)-path exists or not. Vertices are enumerated from `0` to `n-1`.

```python
def check_path_existence(n: int, edges: Dict[int, Set], v: int, u: int) -> bool:
    """
    Returns True/False depending on the existence of an eligible path from vertex v to vertex u in a directed graph.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    E.g. you have a graph with 5 vertices from 0 to 5 and edges {1: {0, 3}, 0: {2}, 3: {4}}.
    There is a path from vertex 1 to vertex 4: 1 -> 3 -> 4, so for v=1 and u=4 function should return True.
    At the same time no path exist from vertex 2 to vertex 0, the expected result is False.

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
        v (int): start path vertex
        u (int): end path vertex
    Returns:
        bool: True or False depending on (v,u)-path existence
    """
```

**Example 1:**
```mermaid
graph TD;
    A((0)) --> B((1));
    B --> C((2));
    A --> D((3));
    E((4));
    F((5));
    F --> D;
```
`v` = 0, `u` = 2

Expected result: True


**Example 2:**
```mermaid
graph TD;
    A((0)) --> B((1));
    B --> C((2));
    A --> D((3));
    E((4));
    F((5));
    F --> D;
```
`v` = 3, `u` = 1

Expected result: False


Please use a template for the implementation (`tasks/path_existence:check_path_existence`).


### Exercise 2: Check if an undirected connected graph is bipartite

Given the number of vertices `n` and graph edges (adjacency dictionary) `edges` for an undirected connected graph, impelemnt the function given below that returns True if graph is bipartite, otherwise False. Vertices are enumerated from `0` to `n-1`. 

```python
def check_bipartite_graph(n: int, edges: Dict[int, Set]) -> bool:
    """
    Returns True/False if a connected undirected graph is bipartite or not.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    E.g. you have a graph with 5 vertices from 0 to 5 and edges {0: {1}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3}.
    This graph is bipartite, because we can select 2 sets of vertices: {0, 2, 4} and {1, 3}, which don't have inner edges.

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
    Returns:
        bool: True or False if a graph is bipartite or not
    """
```

**Example 1:**
```mermaid
graph TD;
    A((0)) ---- B((1));
    B ---- C((2));
    A ---- D((3));
    E((4));
    F((5));
    F ---- D;
    B ---- E;
```

Expected result: True.

**Example 2:**
```mermaid
graph TD;
    A((0)) ---- B((1));
    B ---- H((6));
    B ---- C((2));
    E((4));
    F((5));
    F ---- D((3));
    C ---- E;
    E ---- F;
    H ---- F;
```

Expected result: False.

**Example 3:**
```mermaid
graph TD;
    A((0)) ---- B((1));
    B ---- H((6));
    B ---- C((2));
    E((4));
    F((5));
    F ---- D((3));
    C ---- E;
    E ---- F;
    H ---- I((7));
    I ---- F;
```

Expected result: True.

Please use a template for the implementation (`tasks/bipartite_graph:check_bipartite_graph`).


### Exercise 3: Find the length of the longest eligible path in a directed acyclic graph

Given the number of vertices `n`, graph edges (adjacency dictionary) `edges` for a directed acyclic graph, implement the function given below that returns the length of the longest eligible path. Vertices are enumerated from `0` to `n-1`.

```python
def find_the_longest_path_in_dag(n: int, edges: Dict[int, Set]) -> int:
    """
    Returns the length of the longest path in a directed acyclic graph.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    E.g. you have a graph with 5 vertices from 0 to 5 and edges {4: {3}, 3: {2}, 2: {1}, 1: {0}}.
    The longest path is (4, 0)-path: 4 -> 3 -> 2 -> 1 -> 0. Expected result is 4.

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
    Returns:
        int: length of the longest eligible path in a graph
    """
```

**Example 1:**
```mermaid
graph TD;
    A((0)) --> B((1));
    B --> C((2));
    A --> D((3));
    E((4));
    F((5));
    F --> D;
```

Expected result: 2

**Example 2:**
```mermaid
graph TD;
    A((0)) --> B((1));
    B --> C((2));
    D((3));
    E((4));
    F((5));
    F --> D;
    C --> F;
    A --> H((5));
    H --> D;
```

Expected result: 4

**Example 3:**
```mermaid
graph TD;
    A((0)) --> B((1));
    B --> C((2));
    D((3));
    E((4));
    F((5));
    F --> D;
    C --> F;
    D --> E;
    A --> H((5));
    H --> D;
```

Expected result: 5


Please use a template for the implementation (`tasks/longest_path:find_the_longest_path_in_dag`).
