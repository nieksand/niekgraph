"""
Tests for ufind module.
"""
import unittest

from ufind import UnionFind


class UnionFindTests(unittest.TestCase):
    """
    Tests for ufind module.
    """

    def test_bad_ctor(self):
        """
        Invalid element count should raise.
        """
        with self.assertRaises(ValueError):
            UnionFind(0)
        with self.assertRaises(ValueError):
            UnionFind(-1)

    def test_initial_sets(self):
        """
        Initially every element has unique set. 
        """
        n = 10
        uf = UnionFind(n)
        self.assertEqual(uf.num_sets(), n)

        for idx in range(n):
            self.assertEqual(uf.find(idx), idx)

    def test_union_self(self):
        """
        Union of set against self is no-op.
        """
        uf = UnionFind(3)
        self.assertEqual(uf.num_sets(), 3)

        # expected sets: {0,1} {2}
        def unions_consistent():
            self.assertEqual(uf.num_sets(), 2)
            self.assertEqual(uf.find(0), uf.find(1))
            self.assertNotEqual(uf.find(0), uf.find(2))

        uf.union(0, 1)
        unions_consistent()

        uf.union(1, 0)
        unions_consistent()

    def test_depth_growth_shallow(self):
        """
        Merging single element sets should max at 2 levels.
        """
        n = 100
        uf = UnionFind(n)

        for i in range(1, n):
            uf.union(i-1, i)
        self.assertEqual(uf.num_sets(), 1)

        for i in range(n):
            depth = 0
            j = i
            while uf.parents[j] != j:
                j = uf.parents[j]
                depth += 1
            self.assertLess(depth, 2)

    def test_depth_worst_case(self):
        """
        Worst case expects depth O(lg n).
        """
        n = 8
        uf = UnionFind(n)

        uf.union(0, 1)  # {0,1} {2} {3} {4} {5} {6} {7}
        uf.union(2, 3)  # {0,1} {2,3} {4} {5} {6} {7}
        uf.union(4, 5)  # {0,1} {2,3} {4,5} {6} {7}
        uf.union(6, 7)  # {0,1} {2,3} {4,5} {6,7}

        uf.union(1,2)   # {0,1,2,3} {4,5} {6,7}
        uf.union(4,7)   # {0,1,2,3} {4,5,6,7}

        uf.union(1,7)   # {0,1,2,3,4,5,6,7}

        for i in range(n):
            depth = 0
            j = i
            while uf.parents[j] != j:
                j = uf.parents[j]
                depth += 1
            self.assertLessEqual(depth, 3)

    def test_visualize(self):
        """
        Verify line count equals set count.
        """
        uf = UnionFind(4)
        uf.union(1,3)
        self.assertEqual(uf.num_sets(), 3)
        print(uf.visualize())
        self.assertEqual(uf.visualize().split('\n'), 3)
