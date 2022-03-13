"""
Union-Find data structure.
"""
from io import StringIO
from typing import Dict, List


class UnionFind:
    """
    Union-Find data structure.

    It allows for O(log n) membership lookups and O(log n) unions.
    """

    def __init__(self, n: int):
        """
        Initialize.

        `n`: number of elements to track.
        """
        if n <= 0:
            raise ValueError('invalid element count')

        self.parents = list(range(n))
        self.set_sz = [1] * n

    def find(self, idx: int) -> int:
        """
        Find set id for element.

        `idx`: element index.

        Returns set id.
        """
        while self.parents[idx] != idx:
            idx = self.parents[idx]
        return idx

    def union(self, a: int, b: int) -> None:
        """
        Union of two sets.

        `a`: index of any element in first set
        `b`: index of any element in second set.

        The larger set becomes the parent in order to minimize tree depth.
        (Child set has all nodes increase by one depth level).
        """
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return

        parent, child = (a, b) if self.set_sz[a] > self.set_sz[b] else (b, a)
        self.parents[child] = parent
        self.set_sz[parent] += self.set_sz[child]

    def num_sets(self) -> int:
        """
        Count number of sets.
        """
        return sum(1 for i, v in enumerate(self.parents) if i==v)

    def visualize(self) -> str:
        """
        Visualize sets.

        This inefficient call is intended for debugging purposes. It generates
        output rows like:

            d_0=(depth 0 elements) ... d_n=(depth n elements)
        """
        # gather depth and element by set id
        groups: Dict[int, Dict[int, List[int]]] = {}
        for i in range(len(self.parents)):
            depth = 0
            j = i
            while self.parents[j] != j:
                j = self.parents[j]
                depth += 1

            grp = groups.setdefault(j, {})
            grp.setdefault(depth, []).append(i)

        with StringIO() as buf:
            for group in groups.values():
                for depth, elements in sorted(group.items()):
                    elements.sort()
                    buf.write(f'd_{depth}=(')
                    buf.write(','.join(str(e) for e in elements))
                    buf.write(') ')
                buf.write('\n')

            return buf.getvalue()
