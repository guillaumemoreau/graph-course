import unittest 
import igraph as ig
from network2tikz import plot

import mstgreedy

class GreedyTest(unittest.TestCase):

    """Vérification du comportement des fonctions intermédiaires""" 
    def test_pas_rouge2(self):
        gtest = ig.Graph([(0, 1), (0, 2), (2, 3), (3, 4),
                   (4, 2), (2, 5), (5, 0), (6, 3), (5, 6)])
        gtest.es["pds"] = [1,3,2,4,5,0,1,9,3]
        # on colorie tout en noir
        for e in gtest.es:
            e["acm"] = False

        mstgreedy.draw_coupe(gtest,[],"testgreedy.pdf")
        # aucun label ACM et coupe vide
        self.assertEqual(mstgreedy.pas_de_rouge(gtest,[]),True)
        # on met quelques sommets dans la coupe
        coupe1 = []
        coupe1.append(gtest.vs[0])
        coupe1.append(gtest.vs[2])
        coupe1.append(gtest.vs[3])
        mstgreedy.draw_coupe(gtest, coupe1, "testgreedy1.pdf")
        self.assertEqual(mstgreedy.pas_de_rouge(gtest, coupe1), True)

        # on ajoute quelques arcs rouges 
        gtest.es[3]["acm"] = True 
        gtest.es[4]["acm"] = True
        mstgreedy.draw_coupe(gtest, coupe1, "testgreedy2.pdf")
        self.assertEqual(mstgreedy.pas_de_rouge(gtest, []), True)
        self.assertEqual(mstgreedy.pas_de_rouge(gtest, coupe1), False)
unittest.main()
