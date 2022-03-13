"""
Adjacency list for graph.
"""
from collections import defaultdict
from typing import DefaultDict, Hashable, Iterable, List, Union, Tuple


Node = Union[Hashable, int]


class AdjList:
    """
    Adjacency list for graph.
    """

    def __init__(self, *, is_directed: bool):
        """
        Initialize.
        """
        self.is_directed = is_directed

        self.adjlist: DefaultDict[Node, List[Node]] = defaultdict(list)

    def add_edge(self, src: Node, dst: Node) -> None:
        """
        Add edge to graph.

        `src`: source node
        `dst`: destination node
        """
        self.adjlist[src].append(dst)
        if not self.is_directed:
            self.adjlist[dst].append(src)

    def adjacencies(self) -> Iterable[Tuple[Node, List[Node]]]:
        """
        Iterate over all adjacencies.

        Returns iterator of (src node, [..dst nodes..]) tuples.
        """
        return self.adjlist.items()
