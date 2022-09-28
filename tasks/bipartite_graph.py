"""Template for programming assignment: check if a given connected undirected graph is bipartite or not"""
from typing import Dict, Set


def check_bipartite_graph(n: int, edges: Dict[int, Set]) -> bool:
    """
    Returns True/False if a connected undirected graph is bipartite or not.
    Vertices are enumerated from 0 to N-1, there N - number of vertices.

    E.g. you have a graph with 5 vertices from 0 to 5 and edges {0: {1}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3}.
    This graph is bipartite, because we can select 2 sets of vertices: {0, 2, 4} and {1, 3}, which don't have inner edges.

    Parameters:
        n (int) : number of vertices in the graph, vertices are enumerated from 0 to n-1
        edges (Dict[int, Set]): adjacency dictionary which stores set of adjacent vertices for each vertex
    Returns:
        bool: True or False if graph is bipartite or not
    """

