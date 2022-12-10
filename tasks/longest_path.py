"""Template for programming assignment: find the length of the longest path in a directed acyclic graph."""
from typing import Dict, Set


def find_the_longest_path_in_dag(n: int, edges: Dict[int, Set]) -> int:
    """
    Returns the length of the longest path in a directed acyclic graph.
    Vertices are enumerated from 0 to N-1, where N is the number of vertices.

    For example, you have a graph with five vertices from 0 to 5 and the edges {4: {3}, 3: {2}, 2: {1}, 1: {0}}.
    The longest path is (4, 0)-path: 4 -> 3 -> 2 -> 1 -> 0. The expected result is 4.

    Parameters:
        n (int) : the number of vertices in the graph; vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores a set of adjacent vertices for each vertex
    Returns:
        int: the length of the longest eligible path in a graph
    """
    pass
