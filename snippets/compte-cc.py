import igraph as ig
from network2tikz import plot

# construction du graphe exemple tiré du cours de DP
g1 = ig.Graph(6, [(0, 1), (0, 3), (1, 3), (2, 8),
                  (4, 5), (5, 6), (6, 7)], False)
g1.vs["name"] = ["1", "2", "3", "4", "5", "6","7","8","9"]

# style de dessin
visual_style = {}
visual_style['vertex_label'] = g1.vs['name']
#visual_style['vertex_color'] = 'blue'
visual_style['edge_width'] = 2
visual_style['node_size'] = .8
visual_style['standalone'] = False
visual_style['edge_curved'] = 0.1
visual_style['node_opacity'] = 0.5
color_dict = {0: 'blue', 1: 'red', 2: 'green', 3: 'black'}
layout = {
    0: (0., 0.),
    1: (0., -1.),
    2: (1., -1.),
    3: (1., 0.),
    4: (2., 0.),
    5: (2., -1.),
    6: (2., -2.),
    7: (1.,-2.),
    8: (0,-2)
}
visual_style['layout'] = layout


def visite(i,numcc):
#    global counter
    i["vu"] = True
    i["cc"] = numcc
    # à chaque fois qu'on visite un sommet, on exporte le graphe
#    filename = 'pp-{cc}.tex'.format(cc=counter)
#    visual_style['vertex_color'] = [color_dict[g] for g in g1.vs["vu"]]
#    plot(g1, filename, **visual_style)
#    counter = counter+1
    for j in g1.successors(i):
        if g1.vs[j]["vu"] == False:
            visite(g1.vs[j],numcc)

def compte_cc():
    for s in g1.vs:
        s["vu"] = False 
    cc = 0
    for i in g1.vs:
        if i["vu"] == False:
            cc = cc + 1
            visite(i,cc)
    return cc 

print('G1 a {cc} composantes connexes'.format(cc = compte_cc()))
visual_style['vertex_color'] = [color_dict[g] for g in g1.vs["cc"]]
plot(g1,"compte-cc.tex",**visual_style)