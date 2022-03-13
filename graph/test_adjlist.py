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
