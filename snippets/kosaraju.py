import igraph as ig
from network2tikz import plot

import mygraphs



# chargement du graphe
g1, visual_style = mygraphs.build_graph_exemple_24dense(True)
visual_style['canvas'] = (9, 6)
color_dict = {0: 'blue', 1: 'red', 2: 'green', -1: 'black', 3: 'magenta', 4:'yellow', 5: 'cyan',
              6: 'purple', 7: 'brown', 8: 'lime', 9: 'teal', 10: 'red', 11: 'darkgray', 12: 'gray',
              13: 'pink', 14: 'violet', 15: 'orange', 16: 'black'}


gn = 1

def export_graphe(graphe):
    global gn
    filename = 'kosaraju-{cc}.tex'.format(cc=gn)
    visual_style['vertex_color'] = [color_dict[g] for g in graphe.vs["vu"]]
    plot(graphe, filename, **visual_style)
    gn = gn+1


# Parcours en profondeur avec stockage de l'ordre suffixe 
def visite(g,i):
    global ordre_suffixe
    global counter
    i["vu"] = True
    i["date"] = str(counter)
    counter = counter + 1
    # à chaque fois qu'on visite un sommet, on exporte le graphe
    visual_style['node_label'] = g.vs["date"]
    export_graphe(g)
    for j in g.successors(i):
        if g.vs[j]["vu"] == False:
            visite(g,g.vs[j])
    ordre_suffixe.append(i["nom"])


def DFSUtil(ginv, v, ncb):
    v["vu"] = True
    v["comp"] = ncb
    export_graphe(ginv)
    for i in v.successors():
        if i["vu"] == False:
            DFSUtil(ginv, i, ncb)

# initialisation
counter = 1
for s in g1.vs:
    s["vu"] = False
    s["nom"] = str(counter)
    s["date"] = ""
    counter = counter + 1
visual_style['node_label'] = g1.vs["nom"]
ordre_suffixe = []
# sauvegarde du graphe originel
plot(g1, 'kosaraju-0.tex', **visual_style)
counter = 1
for i in g1.vs:
    if i["vu"] == False:
        visite(g1,i)

print(ordre_suffixe)
plot(g1,'kosaraju-p1.tex',**visual_style)


#inversion du graphe 
ginv = ig.Graph(24,[],True)
n = 1
for v in ginv.vs:
    v["nom"] = str(n) 
    v["vu"] = False 
    v["date"] = ""
    n = n + 1
for e in g1.es: 
    ginv.add_edge(e.target,e.source)

visual_style['node_label'] = ginv.vs["nom"]
plot(ginv, 'kosaraju-inverse.tex', **visual_style)


ncb = 1

while ordre_suffixe:
    i = ordre_suffixe.pop()
    e = ginv.vs.select(nom = i)[0]
    if (e["vu"] == False):
        e["comp"] = ncb
        DFSUtil(ginv,e,ncb)
        ncb = ncb+1
        print("/") 


visual_style['node_label'] = ginv.vs["comp"]
visual_style['vertex_color'] = [color_dict[g] for g in ginv.vs["comp"]]
plot(ginv, 'kosaraju-cfc.tex', **visual_style)
