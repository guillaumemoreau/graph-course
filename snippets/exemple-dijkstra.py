import igraph as ig
from network2tikz import plot
import mygraphs
import math
import dijkstra


g = mygraphs.build_exemple_pcc()
print(g)
visual_style = {}
visual_style['edge_width'] = 2
visual_style['node_size'] = .8
visual_style['standalone'] = False
visual_style['node_opacity'] = 0.5
visual_style['vertex_label'] = g.vs["name"]
visual_style['edge_label'] = g.es["w"]
visual_style['canvas'] = (9, 6)
layout = {
    0: (-1, -1),
    1: (1, 0),
    2: (1, -4),
    3: (2, -2),
    4: (3, -3),
    5: (5, 0),
    6: (5, -3),
    7: (6, -4)
}
visual_style['layout'] = layout
plot(g, 'dijkstra-0.pdf', **visual_style)
dijkstra.dijkstra(g, g.vs.find(name="s"))
