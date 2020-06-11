# génération d'un exemple pour le cours 

import igraph as ig
from network2tikz import plot
import random 

taille = 30
g = ig.Graph.GRG(taille,.35)

# style de dessin
visual_style = {}
#visual_style['vertex_label'] = g1.vs['name']
#visual_style['vertex_color'] = 'blue'
#visual_style['edge_width'] = .3
visual_style['node_size'] = .2
#visual_style['standalone'] = False
#visual_style['edge_curved'] = 0.1
visual_style['node_opacity'] = 0.5
#visual_style['canvas'] = (12,8)
color_dict = {True: 'blue', False: 'black'}
visual_style['layout'] = 'kk'

ig.plot(g, 'mst-0.pdf', **visual_style)


# MST inclus dans le graphe 
for e in g.es:
    e["mst"] = False

mst = g.spanning_tree(None,False)

for eid in mst:
    g.es[eid]["mst"] = True

visual_style['edge_color'] = [color_dict[g] for g in g.es["mst"]]
ig.plot(g, 'mst-1.pdf', **visual_style)

# MST seul
color_dict2 = {True: 'blue', False: 'white'}
visual_style['edge_color'] = [color_dict2[g] for g in g.es["mst"]]
ig.plot(g, 'mst-2.pdf', **visual_style)


# on recommence avec un graphe pondéré
taille2 = 10
conn = False
while conn == False:
    g2 = ig.Graph.GRG(taille2,.55)
    conn = g2.is_connected()
visual_style = {}
visual_style['node_size'] = .2
visual_style['node_opacity'] = 0.5
visual_style['layout'] = 'kk'
ponderation = []
for e in g2.es:
    a = random.randrange(10)
    e["pds"] = a 
    ponderation.append(a)
visual_style['edge_label'] = g2.es["pds"]
ig.plot(g2,'mstp-0.pdf',**visual_style)
for e in g2.es:
    e["mst"] = False 
mst = g2.spanning_tree(ponderation,False)
for eid in mst:
    g2.es[eid]["mst"] = True
visual_style['edge_color'] = [color_dict[g] for g in g2.es["mst"]]
ig.plot(g2, 'mstp-1.pdf', **visual_style)
