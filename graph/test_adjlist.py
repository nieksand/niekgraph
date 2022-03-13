"""
Test for adjlist module.
"""
import unittest

from adjlist import AdjList


class AdjListTests(unittest.TestCase):
    """
    Test for adjlist module.
    """

    def test_add_edge_directed(self):
        """
        Directed graphs add adjacency in one direction.
        """
        alist = AdjList(is_directed=True)
        self.assertEqual(len(alist.adjacencies()), 0)

        alist.add_edge(0, 1)
        self.assertEqual(len(alist.adjacencies()), 1)

    def test_add_edge_undirected(self):
        """
        Undirected graphs add adjacency in both directions.
        """
        alist = AdjList(is_directed=False)
        self.assertEqual(len(alist.adjacencies()), 0)

        alist.add_edge(0, 1)
        self.assertEqual(len(alist.adjacencies()), 2)

    def test_adjacencies(self):
        """
        Expect iterable over src to dst lists.
        """
        alist = AdjList(is_directed=True)
        alist.add_edge(0, 1)
        alist.add_edge(0, 3)
        alist.add_edge(0, 2)
        alist.add_edge(2, 3)

        output = dict(alist.adjacencies())
        self.assertEqual({0, 2}, output.keys())
        self.assertEqual(set(output[0]), {1, 2, 3})
        self.assertEqual(set(output[2]), {3})
