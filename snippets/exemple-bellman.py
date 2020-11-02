import igraph as ig
from network2tikz import plot
import mygraphs
import math
import bellman


g = mygraphs.build_exemple_bellmann()
print(g)
visual_style = {}
visual_style['edge_width'] = 2
visual_style['node_size'] = .8
visual_style['standalone'] = False
visual_style['node_opacity'] = 0.5
visual_style['vertex_label'] = g.vs["name"]
visual_style['edge_label'] = g.es["w"]
visual_style['canvas'] = (9,6)
layout = { 
    0: (-1,0),
    1: (2,1),
    2: (2,-1),
    3: (4,0),
    4: (3,-3),
    5: (6,-1),
}
visual_style['layout'] = layout
plot(g,'bellmann-0.pdf',**visual_style)
bellman.bellman(g,g.vs.find(name="1"))
