# parcours en profondeur

import igraph as ig 
from network2tikz import plot

# construction du graphe exemple tiré du cours de DP
g1 = ig.Graph(6, [(0, 1), (0, 3), (1, 3), (1, 2), (2, 3), (3, 2), (5, 4)],True)
g1.vs["name"] = ["1","2","3","4","5","6"]
g1.vs["vu"] = [False,False,False,False,False]

# style de dessin
visual_style = {}
visual_style['vertex_label'] = g1.vs['name']
#visual_style['vertex_color'] = 'blue'
visual_style['edge_width'] = 2
visual_style['node_size'] = .8
visual_style['standalone'] = False
visual_style['edge_curved'] = 0.1
visual_style['node_opacity'] = 0.5
color_dict = {True: 'blue',False:'red'}
layout = {
    0: (0.,0.),
    1: (0.,-1.),
    2: (1.,-1.),
    3: (1.,0.),
    4: (2.,0.),
    5: (2.,-1.),
}
visual_style['layout'] = layout

# ig.plot(g1, **visual_style)

plot(g1,'pp-0.tex',**visual_style)


counter = 1

def visite(i,depth):
    global counter
    i["vu"] = True
    # à chaque fois qu'on visite un sommet, on exporte le graphe
    filename = 'pp-{cc}.tex'.format(cc=counter)
    visual_style['vertex_color'] = [color_dict[g] for g in g1.vs["vu"]]
    plot(g1, filename,**visual_style)
    counter = counter+1
    for j in g1.successors(i):
        if g1.vs[j]["vu"] == False:
            visite(g1.vs[j],depth+1)

for i in g1.vs:
    if i["vu"] == False:
        visite(i,0)

