import igraph as ig
from network2tikz import plot

# petit graphe à 8 sommets pour les CFC 
def build_graph_exemple_8(oriente = True):
    g1 = ig.Graph(8,[(0,2),(1,2),(2,3),(3,2),(4,1),(1,4),(1,5),(5,6),(6,5),(2,6),(6,7),(3,7)],oriente)
    visual_style = {}
    visual_style['edge_width'] = 2
    visual_style['node_size'] = .8
    visual_style['standalone'] = False
    visual_style['node_opacity'] = 0.5

    # layout grille
    layout = {}
    for y in range(0, 1):
        for x in range(0, 3):
            layout[y*4+x] = (x, -y)
    visual_style['layout'] = layout

    return g1,visual_style

# construction du graphe exemple tiré du cours de DP
def build_graph_exemple_24(oriente = False):
    g1 = ig.Graph(24, [(0, 6), (6, 12), (12, 18), (7, 13), (13, 19), (2, 8), (8, 14), (3, 9), (15, 21), (4, 10), (10, 16), (5, 11), (11, 17),
                   (6, 7), (7, 8), (8, 9), (9, 10), (12, 13), (13, 14), (16, 17), (18, 19), (20, 21), (22, 23)], oriente)
    visual_style = {}
    visual_style['edge_width'] = 2
    visual_style['node_size'] = .8
    visual_style['standalone'] = False
    visual_style['node_opacity'] = 0.5

    # layout grille
    layout = {}
    for y in range(0, 4):
        for x in range(0, 6):
            layout[y*6+x] = (x, -y)
    visual_style['layout'] = layout

    # numérotation des sommets
    # counter = 1
    # g1.vs["name"] = ["1"]
    # first = True
    # for s in g1.vs:
    #     if first:
    #         first = False
    #     else:
    #         g1.vs["name"].append(str(counter))
    #         print(counter)
    #     counter = counter + 1

    # print(g1.vs["name"])
    return g1,visual_style


# construction du graphe exemple tiré du cours de DP
def build_graph_exemple_24dense(oriente=False):
    g1 = ig.Graph(24, [(0, 6), (6, 12), (12, 18), (7, 13), (19, 13), (2, 8), (14, 8), (3, 9), (15, 21), (4, 10), (10, 16), (5, 11), (11, 17),
                       (6, 7), (8, 7), (8, 9), (9, 10), (12, 13), (13, 14), (16, 17), (18, 19), (20, 21), (22, 23),
                       (8,2),(13,6)], oriente)
    visual_style = {}
    visual_style['edge_width'] = 2
    visual_style['node_size'] = .8
    visual_style['standalone'] = False
    visual_style['node_opacity'] = 0.5

    # layout grille
    layout = {}
    for y in range(0, 4):
        for x in range(0, 6):
            layout[y*6+x] = (x, -y)
    visual_style['layout'] = layout

    # numérotation des sommets
    # counter = 1
    # g1.vs["name"] = ["1"]
    # first = True
    # for s in g1.vs:
    #     if first:
    #         first = False
    #     else:
    #         g1.vs["name"].append(str(counter))
    #         print(counter)
    #     counter = counter + 1

    # print(g1.vs["name"])
    return g1, visual_style


def build_graph_exemple_6():
    g1 = ig.Graph(6, [(0, 1), (0, 3), (1, 3), (2, 8),
                    (4, 5), (5, 6), (6, 7)], False)
    g1.vs["name"] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

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
        7: (1., -2.),
        8: (0, -2)
    }
    visual_style['layout'] = layout
    return g1,visual_style
