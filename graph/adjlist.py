"""
Adjacency list for graph.
"""
from collections import defaultdict
from typing import Any, DefaultDict, Iterator, List, Tuple


class AdjList:
    """
    Adjacency list for graph.
    """

    def __init__(self, *, is_directed: bool):
        """
        Initialize.    
        """
        self.is_directed = is_directed

        self.adjacencies: DefaultDict[Any, List[Any]] = defaultdict(list)

    def add_edge(self, src: Any, dst: Any) -> None:
        """
        Add edge to graph.

        `src`: source node
        `dst`: destination node
        """
        self.adjacencies[src].append(dst)
        if not self.is_directed:
            self.adjacencies[dst].append(src)

    def adjacencies(self) -> Iterator[Tuple[Any, List[Any]]]:
        """
        Get iterator over adjacencies.

        Returns iterator emitting (src edge, [...dst edges]) tuples.
        """
        return self.adjacencies.items()
