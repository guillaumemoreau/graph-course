import igraph as ig
from network2tikz import plot

import mygraphs



# chargement du graphe
g1, visual_style = mygraphs.build_graph_exemple_24(True)

# Parcours en profondeur avec stockage de l'ordre suffixe 


def visite(i):
    global ordre_suffixe
    i["vu"] = True
    for j in g1.successors(i):
        if g1.vs[j]["vu"] == False:
            visite(g1.vs[j])
    ordre_suffixe.append(i["nom"])

counter = 1
for s in g1.vs:
    s["vu"] = False
    s["nom"] = str(counter)
    counter = counter + 1
ordre_suffixe = []
for i in g1.vs:
    if i["vu"] == False:
        visite(i)
print(ordre_suffixe)

    visual_style['node_label'] = g1.vs["nom"]
plot(g1,'kosaraju-1.tex',**visual_style)
