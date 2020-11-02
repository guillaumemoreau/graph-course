# génération d'un exemple pour le cours

import igraph as ig
from network2tikz import plot
import random
import mygraphs

taille = 15


nb_colored = 0 

def draw_coupe(graphe,coupe,filename):
    for s in graphe.vs:
        s["coupe"] = False 
    for s in coupe:
        s["coupe"] = True
    color_dict = {True: 'red', False: 'black'}
    coupe_dict = {True: 'red', False: 'blue'}
    visual_style = {}
    visual_style['node_size'] = .2
    visual_style['node_opacity'] = 0.5
    visual_style['layout'] = 'kk'
    visual_style['vertex_color'] = [coupe_dict[g] for g in graphe.vs["coupe"]]
    visual_style['edge_color'] = [color_dict[g] for g in graphe.es["acm"]]
    visual_style['edge_label'] = graphe.es["pds"]
    ig.plot(graphe, filename, **visual_style)


def pas_de_rouge(graphe,coupe):
    for a in graphe.es:
        if (a["acm"] == True):
            b1 = a.source_vertex in coupe 
            b2 = a.target_vertex in coupe 
            if (b1 != b2):
                return False
    return True

ncoupe = 1
def get_coupe(graphe):
    global ncoupe
    global taille
    # définir une coupe au hasard
    valid = False
    attempt = 1 
    while valid ==False:
        coupe = []
        for s in graphe.vs: 
            b = random.randrange(2)
            if b == 0:
                coupe.append(s)
        print('taille S1 : '+str(len(coupe)))
        if (len(coupe) > 0) and (len(coupe) < taille) and pas_de_rouge(graphe,coupe):
            assert(len(coupe) < taille)
            print('ok at attempt:'+str(attempt))
            #draw_coupe(graphe,coupe,'tmp/coupe-'+str(ncoupe)+'.pdf')
            ncoupe = ncoupe + 1
            valid = True
        attempt = attempt+1
    return coupe

nb = 1
g,visual_style = mygraphs.gen_graphe_connexe(taille)
while nb_colored < taille-1:
    # on cherche une coupe valide 
    coupe = get_coupe(g)

    filename = 'tmp/mst-greedy-' + str(nb) + '.pdf'
    draw_coupe(g, coupe, filename)
    nb = nb + 1 

    #choisir l'arête traversante de poids minimal 
    pmin = 9999999999999
    for a in g.es: 
        if a["acm"] == False:
            b1 = a.source_vertex in coupe
            b2 = a.target_vertex in coupe
            if (b1 != b2): # l'arête est traversante
                if (a["pds"] < pmin):
                    emin = a
                    pmin = a["pds"]
    print(pmin)

    # on la colorie en rouge 
    emin["acm"] = True 

    filename = 'tmp/mst-greedy-' + str(nb) + '.pdf'
    draw_coupe(g, coupe, filename)
    nb = nb+1 
    nb_colored = nb_colored +1
