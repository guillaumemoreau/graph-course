# génération d'un exemple pour le cours

import igraph as ig
from network2tikz import plot
import random
import mygraphs

taille = 15


nb_colored = 0 

def draw_coupe(graphe,filename):
    color_dict = {True: 'red', False: 'black'}
    coupe_dict = {True: 'red', False: 'blue'}
    visual_style = {}
    visual_style['node_size'] = .2
    visual_style['node_opacity'] = 0.5
    visual_style['layout'] = 'kk'
    visual_style['vertex_color'] = [coupe_dict[g] for g in graphe.vs["col"]]
    visual_style['edge_color'] = [color_dict[g] for g in graphe.es["acm"]]
    visual_style['edge_label'] = graphe.es["pds"]
    ig.plot(graphe, filename, **visual_style)


def existe_sommet_noir(g):
    for s in g.vs:
        if s["col"] == False:
            return True
    return False

nb = 1
g,visual_style = mygraphs.gen_graphe_connexe(taille)

# on colorie tout en noir
for s in g.vs:
    s["col"] = False
for a in g.es:
    a["acm"] = False
g.vs[0]["col"] = True  # sommet de départ

draw_coupe(g,'mstprim-0.pdf')
while existe_sommet_noir(g):
    #choisir l'arête traversante de poids minimal
    pmin = 9999999999999
    emin = g.es[0]
    for a in g.es:
        if a["acm"] == False:
            b1 = a.source_vertex["col"]
            b2 = a.target_vertex["col"]
            if (b1 != b2):  # l'arête est traversante
                if (a["pds"] < pmin):
                    emin = a
                    pmin = a["pds"]
    emin["acm"] = True
    emin.source_vertex["col"] = True
    emin.target_vertex["col"] = True 
    draw_coupe(g,'mstprim-'+str(nb)+'.pdf')
    nb = nb+1



