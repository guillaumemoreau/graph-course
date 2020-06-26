import igraph as ig
from network2tikz import plot
import random 

# exemple de graphe pour FF 
def build_exemple_ff():
    g = ig.Graph(8,[],True)
    g.vs["name"] = ["s","A","B","C","D","E","F","t"]
    g.add_edge(0,1)["c"] = 35
    g.add_edge(0,2)["c"] = 35
    g.add_edge(0,3)["c"] = 40
    g.add_edge(1,4)["c"] = 20
    g.add_edge(1,6)["c"] = 10
    g.add_edge(2,4)["c"] = 15
    g.add_edge(2,5)["c"] = 25
    g.add_edge(2,6)["c"] = 5
    g.add_edge(3,5)["c"] = 20
    g.add_edge(3,6)["c"] = 20
    g.add_edge(4,7)["c"] = 20
    g.add_edge(5,7)["c"] = 30
    g.add_edge(6,7)["c"] = 60

    return g


# graphe acyclique pour les PCC 
def build_exemple_pcc():
    g = ig.Graph(8,[],True)
    g.vs["name"] = ["s","2","7","6","5","3","4","t"]
    g.add_edge(0,1)["w"] = 9
    g.add_edge(0,3)["w"] = 14
    g.add_edge(0,2)["w"] = 15
    g.add_edge(1,5)["w"] = 24
    g.add_edge(3,5)["w"] = 18
    g.add_edge(3,2)["w"] = 5
    g.add_edge(3,4)["w"] = 30
    g.add_edge(3,5)["w"] = 18
    g.add_edge(5,4)["w"] = 2
    g.add_edge(5,7)["w"] = 19
    g.add_edge(4,6)["w"] = 11
    g.add_edge(4,7)["w"] = 16
    g.add_edge(6,7)["w"] = 6
    g.add_edge(2,7)["w"] = 44 
    g.add_edge(2,4)["w"] = 20

    # (0,1),(0,6),(0,7),(1,5),(3,5),(3,4),(3,2),(2,4),(5,4),(4,6),(4,7),(2,7),(6,7),(5,7)]
    return g

# graphe avec cycle et poids négatifs pour l'algo de Bellmann 
def build_exemple_bellmann():
    g = ig.Graph(6,[],True)
    g.vs["name"] = ["1","2","3","4","5","6"]
    g.add_edge(0,1)["w"] = 3
    g.add_edge(0,2)["w"] = 6
    g.add_edge(0,4)["w"] = 3 
    g.add_edge(1,2)["w"] = -3 
    g.add_edge(1,3)["w"] = 6
    g.add_edge(2,3)["w"] = 1
    g.add_edge(4,2)["w"] = -2 
    g.add_edge(3,4)["w"] = 9 
    g.add_edge(3,5)["w"] = 1
    g.add_edge(4,5)["w"] = 5


    return g

# petit graphe a 8 sommets pour les CFC 
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

# construction du graphe exemple tire du cours de DP
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

    # numerotation des sommets
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


# construction du graphe exemple tire du cours de DP
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

    # numerotation des sommets
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

# graphe pour les exemples d'arbres couvrants minimaux
def gen_graphe_connexe(taille):
    conn = False
    while conn == False:
        g = ig.Graph.GRG(taille, .45)
        conn = g.is_connected()
    visual_style = {}
    visual_style['node_size'] = .2
    visual_style['node_opacity'] = 0.5
    visual_style['layout'] = 'kk'
    ponderation = []
    for e in g.es:
        a = random.randrange(10)
        e["pds"] = a
        ponderation.append(a)
    visual_style['edge_label'] = g.es["pds"]
    # on colorie tout en noir
    for e in g.es:
        e["acm"] = False
    return g, visual_style
