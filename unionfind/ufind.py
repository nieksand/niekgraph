"""
Basic Union Find Implementation
"""


class UnionFind:
    """
    Basic Union Find Implementation
    """

    def __init__(self, n):
        """
        Initialize.

        `n`: number of elements to track.
        """
        self.parents = list(range(n))
        self.child_sz = [1] * n


    def find(self, idx):
        """
        Find set id for element.

        `idx`: element index.

        Returns set id.
        """
        while self.parents[idx] != idx:
            idx = self.parents[idx]
        return idx

    def union(self, a, b):
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

        parent, child = (a, b) if self.child_sz[a] > self.child_sz[b] else (b, a)
        self.parents[child] = parent
        self.child_sz[parent] += self.child_sz[child]

    def num_sets(self):
        """
        Count number of sets.
        """
        return sum(1 for i, v in enumerate(self.parents) if i==v)
