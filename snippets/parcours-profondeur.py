# parcours en profondeur

import igraph as ig 
from network2tikz import plot

# construction du graphe exemple tiré du cours de DP
g1 = ig.Graph(24, [(0, 6), (6, 12), (12, 18), (7, 13), (13, 19), (2, 8), (8, 14), (3, 9), (15, 21), (4, 10), (10, 16), (5, 11), (11, 17),
                   (6, 7), (7, 8), (8, 9), (9, 10), (12, 13), (13, 14), (16, 17), (18, 19), (20, 21), (22, 23)], False)
visual_style = {}
#visual_style['vertex_color'] = 'blue'
visual_style['edge_width'] = 2
visual_style['node_size'] = .8
visual_style['standalone'] = False
visual_style['node_opacity'] = 0.5
color_dict = {0: 'blue', 1: 'red', 2: 'green', -1: 'black'}

# layout grille
layout = {}
for y in range(0, 4):
    for x in range(0, 6):
        layout[y*6+x] = (x, -y)
visual_style['layout'] = layout

# ig.plot(g1, **visual_style)

plot(g1,'pp-0.tex',**visual_style)


counter = 1


def export_graphe():
    global counter
    filename = 'pp-{cc}.tex'.format(cc=counter)
    visual_style['vertex_color'] = [color_dict[g] for g in g1.vs["vu"]]
    visual_style['node_label'] = g1.vs["date"]
    plot(g1, filename, **visual_style)
    counter = counter+1


def visite(i,depth):
    global counter
    i["vu"] = True
    i["date"] = str(counter)
    # à chaque fois qu'on visite un sommet, on exporte le graphe
    export_graphe()
    for j in g1.successors(i):
        if g1.vs[j]["vu"] == False:
            visite(g1.vs[j],depth+1)

for s in g1.vs:
    s["vu"] = False 
    s["date"] = ""
for i in g1.vs:
    if i["vu"] == False:
        visite(i,0)

