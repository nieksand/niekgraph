"""
Adjacency list for graph.
"""
from collections import defaultdict
from typing import Dict, Hashable, List


class AdjList:
    """
    Adjacency list for graph.
    """

    def __init__(self, *, is_directed: bool):
        """
        Initialize.    
        """
        self.is_directed = False

        self.adjacencies: Dict[Hashable, List[Hashable]] = defaultdict(list)

    def add_edge(self, src: Hashable, dst: Hashable) -> None:
        """
        Add edge to graph.

        `src`: source node
        `dst`: destination node
        """
        self.adjacencies[src].append(dst)
        if not self.is_directed:
            self.adjacencies[dst].append(src)
