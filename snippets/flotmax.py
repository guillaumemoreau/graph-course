# tous les algorithmes autour du flot max
# on considère des graphes avec des attributs pour les arêtes 
#   c pour la capacité 
#   f pour le flot 

import igraph as ig
import network2tikz 
import mygraphs
import math
from queue import Queue

color_dict = {True: 'blue', False: 'black'}

# construire le graphe résiduel 
def build_graphe_residuel(G):
    Gr = ig.Graph(len(G.vs),[],True)
    counter = 0
    for s in G.vs:
        Gr.vs[counter]["name"] = s["name"]
        counter = counter+1
    
    for e in G.es:
        sn = e.source_vertex["name"]
        dn = e.target_vertex["name"]
        #print(sn+'->'+dn)
        src = Gr.vs.select(name = sn)[0]
        dst = Gr.vs.select(name = dn)[0]
        if e["f"] > 0:
            ne = Gr.add_edge(dst,src)
            ne["c"] = e["f"]
            ne["f"] = 0
            ne["type"] = "-"
        if e["f"] < e["c"]:
            ne = Gr.add_edge(src,dst)
            ne["c"] = e["c"]-e["f"]
            ne["f"] = 0
            ne["type"] = "+"

    return Gr 


def get_sommet_by_name(G,myname):
    s = G.vs.select(name = myname)[0]
    return s

def init_flot(G):
    for e in G.es:
        e["f"] = 0

def build_labels(g,withFlow=True):
    for e in g.es:
        e["label"] = ""
        if withFlow:
            e["label"] = str(e["f"])+' '
        e["label"] = e["label"] +'['+str(e["c"])+']'

def print_edge_properties(g):
    for e in g.es:
        print(e)
    print('---')


def print_vertex_properties(g):
    for v in g.vs:
        print(v)
    print('---')


def BFS_visite(g1,i):
    q = Queue()
    i["vu"] = True
    q.put(i)
    while q.empty() == False:
        k = q.get()
        for j in g1.successors(k):
            if g1.vs[j]["vu"] == False:
                g1.vs[j]["vu"] = True
                g1.vs[j]["from"] = k
                q.put(g1.vs[j])


def path_from_BFS(g1,dep,arr):
    for s in g1.vs:
        s["vu"] = False
        s["from"] = ""
    BFS_visite(g1,dep)
    curr = arr
    path = [ ]
    print(arr["vu"])
    if arr["vu"] == True:
        path.append(arr["name"])
        while curr["name"] != dep["name"]:
            prev = curr["from"]
            path.insert(0,prev["name"])
            curr = prev
    return path
    
def FordFulkerson(G,s,t):
    # on construit un premier graphe résiduel 
    for e in G.es:
        e["dirty"] = False
    iteration = 0
    Gr = build_graphe_residuel(G)
    path = path_from_BFS(Gr, get_sommet_by_name(Gr, "s"), get_sommet_by_name(Gr, "t"))
    print(path)
    while len(path) >0 and path[-1] == t["name"]:
        print("Iteration : "+str(iteration))
        # on sauve le graphe avec le flot en l'état
        build_labels(G, True)
        visual_style['edge_label'] = G.es["label"]
        visual_style['edge_color'] = [color_dict[g] for g in G.es["dirty"]]
        network2tikz.plot(G, 'ff-'+str(iteration)+'.tex', **visual_style)
        build_labels(Gr, False)
        visual_style['edge_label'] = Gr.es["label"]
        visual_style['edge_color'] = 'black'
        network2tikz.plot(Gr, 'ffr-'+str(iteration)+'.tex', **visual_style)
    # on parcourt le chemin pour trouver alpha
        alpha = math.inf
        for sommet in path:
            vs = get_sommet_by_name(Gr, sommet)
            if vs["name"] != "s":
                # on traite l'arc (prev,sommet)
                ps = get_sommet_by_name(Gr, prev)
                # print("traitement de ("+ps["name"]+","+vs["name"]+")")
                found = False
                for edges in Gr.es:
                    if edges.source_vertex["name"] == ps["name"] and edges.target_vertex["name"] == vs["name"]:
                        e = edges
                        found = True
                        alpha = min(alpha, e["c"])
            prev = sommet
        print(alpha)
        # on met à jour le graphe
        for e in G.es:
            e["dirty"] = False
        for sommet in path:
            vs = get_sommet_by_name(G, sommet)
            if vs["name"] != "s":
                # on traite l'arc
                ps = get_sommet_by_name(Gr, prev)
                found = False
                for edges in G.es:
                    if edges.source_vertex["name"] == ps["name"] and edges.target_vertex["name"] == vs["name"]:
                        # arc dans le sens s vers t
                        edges["f"] = edges["f"] + alpha
                        edges["dirty"] = True
                        found = True
                    if edges.source_vertex["name"] == vs["name"] and edges.target_vertex["name"] == ps["name"]:
                        # arc dans le sens t vers s
                        edges["f"] = edges["f"] - alpha
                        edges["dirty"] = True
            prev = sommet

        # on recalcule le graphe résiduel
        Gr = build_graphe_residuel(G)
        path = path_from_BFS(Gr, get_sommet_by_name(Gr, "s"), get_sommet_by_name(Gr, "t"))
        print(path)
        iteration = iteration + 1
    # on sauve le graphe avec le flot en l'état
    build_labels(G, True)
    visual_style['edge_label'] = G.es["label"]
    visual_style['edge_color'] = [color_dict[g] for g in G.es["dirty"]]
    network2tikz.plot(G, 'ff-'+str(iteration)+'.tex', **visual_style)
    build_labels(Gr, False)
    visual_style['edge_label'] = Gr.es["label"]
    visual_style['edge_color'] = 'black'
    network2tikz.plot(Gr, 'ffr-'+str(iteration)+'.tex', **visual_style)

G = mygraphs.build_exemple_ff()
init_flot(G)


visual_style = {}
visual_style['edge_width'] = 1
visual_style['edge_curved'] = 0.15
visual_style['node_size'] = .5
visual_style['standalone'] = False
visual_style['node_opacity'] = 0.5
visual_style['vertex_label'] = G.vs["name"]
build_labels(G)
visual_style['edge_label'] = G.es["label"]
visual_style['canvas'] = (9,6)
layout = { 
    0: (-1,0),
    1: (1,2),
    2: (1,-0.8),
    3: (1,-2),
    4: (3,2),
    5: (3.5,0),
    6: (3,-2),
    7: (5,0)
}
visual_style['layout'] = layout
network2tikz.plot(G, 'ff-0.tex', **visual_style)

FordFulkerson(G,get_sommet_by_name(G,"s"),get_sommet_by_name(G,"t"))

