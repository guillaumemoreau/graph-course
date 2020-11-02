import igraph as ig
from network2tikz import plot
import mygraphs
import math
import bellman


g = mygraphs.build_exo_airlines()
print(g)
visual_style = {}
visual_style['edge_width'] = 2
visual_style['node_size'] = .8
visual_style['standalone'] = False
visual_style['node_opacity'] = 0.5
visual_style['vertex_label'] = g.vs["name"]
visual_style['edge_curved'] = .1
visual_style['edge_label'] = g.es["w"]
visual_style['canvas'] = (9, 6)
layout = {
    0: (-1, -1),
    1: (2, 0),
    2: (1, -4),
    3: (2, -2),
    4: (3, -3),
}
visual_style['layout'] = layout
bellman.bellman(g, g.vs.find(name="A"))

M = g.get_adjacency(2,attribute="w",default=float('inf'))

print(M)

bellman.matrix_bellman(M)


