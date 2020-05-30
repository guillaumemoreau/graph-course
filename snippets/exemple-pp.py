# parcours en profondeur

import igraph as ig 
from network2tikz import plot

# construction d'un graphe aléatoire
taille = 30
g1 = ig.Graph.GRG(taille,.2)
for i in g1.vs:
    i["vu"] = False

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
color_dict = {True: 'blue',False:'red'}
visual_style['layout'] = 'kk'

ig.plot(g1,'rg-0.pdf',**visual_style)


counter = 1

def visite(i,depth):
    global counter
    i["vu"] = True
    # à chaque fois qu'on visite un sommet, on exporte le graphe
    filename = 'rg-{cc}.pdf'.format(cc=counter)
    visual_style['vertex_color'] = [color_dict[g] for g in g1.vs["vu"]]
    ig.plot(g1, filename,**visual_style)
    counter = counter+1
    for j in g1.successors(i):
        if g1.vs[j]["vu"] == False:
            visite(g1.vs[j],depth+1)

for i in g1.vs:
    if i["vu"] == False:
        visite(i,0)

