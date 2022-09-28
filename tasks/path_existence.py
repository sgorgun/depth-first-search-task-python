"""Template for programming assignment:
check if there is an eligible path in a directed graph from given vertex v to given vertex u."""
from typing import Dict, Set


def check_path_existence(n: int, edges: Dict[int, Set], v: int, u: int) -> bool:
    """
    Returns True/False depending on existence of an eligible path from vertex v to vertex u in a directed graph.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    E.g. you have a graph with 5 vertices from 0 to 5 and edges {1: {0, 3}, 0: {2}, 3: {4}}.
    There is a path from vertex 1 to vertex 4: 1 -> 3 -> 4, so for v=1 and u=4 function should return True.
    At the same time no path exist from vertex 2 to vertex 0, expected function result is False.

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores set of adjacent vertices for each vertex
        v (int): start path vertex
        u (int): end path vertex
    Returns:
        bool: True or False depending on (v,u)-path existence
    """



