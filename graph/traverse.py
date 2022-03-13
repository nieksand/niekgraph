"""
Graph traversal algorithms.
"""
from collections import deque
from typing import Callable

from adjlist import Node
from adjlist import AdjList

VisitFn = Callable[[Node], None]


def dfs(alist: AdjList, src: Node, visit_fn: VisitFn) -> None:
    """
    Depth first search.

    `alist`: adjacency list.
    `src`: starting node.
    `visit_fn`: visit function invoked at each first node visit.
    """
    if alist.adjlist.get(src) is None:
        return

    visited = set()

    work = [src]
    while work:
        node = work.pop()
        if node in visited:
            continue

        visit_fn(node)
        visited.add(node)

        for neighbor in alist.neighbors(node):
            work.append(neighbor)


def bfs(alist: AdjList, src: Node, visit_fn: VisitFn) -> None:
    """
    Breadth first search.

    `alist`: adjacency list.
    `src`: starting node.
    `visit_fn`: visit function invoked at each first node visit.
    """
    if alist.adjlist.get(src) is None:
        return

    visited = set()

    work = deque([src])
    while work:
        node = work.popleft()
        if node in visited:
            continue

        visit_fn(node)
        visited.add(node)

        for neighbor in alist.neighbors(node):
            work.append(neighbor)
