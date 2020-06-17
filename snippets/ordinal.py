import igraph as ig 
from network2tikz import plot
import mygraphs 
import math 
from queue import Queue

# construction du tri topologique 
def tri_topologique(G):
    listeSommets = []
    for i in G.vs:
        i["col"] = 0 # 0 pour blanc, 1 pour gris, 2 pour noir 
    
    for x in G.vs:
        if x["col"] == 0:
            pp_topologique(G,listeSommets,x)

    return listeSommets

def pp_topologique(G, listeSommets, x):
    x["col"] = 1
    for i in x.successors():
        if i["col"] == 0:
            pp_topologique(G,listeSommets,i)
    
    x["col"] = 2
    listeSommets.append(x)

def ordinal(G,s):
    ord = tri_topologique(G)
    for i in G.vs:
        i["dist"] = math.inf
        i["pred"] = ""
    while ord:
        i = ord.pop()
        print("processing "+i["name"])
        if (i == s):
            i["dist"] = 0
        else:
            for j in i.predecessors():
                if j["dist"] + G.es[G.get_eid(j,i)]["w"] < i["dist"]:
                    i["dist"] = j["dist"] + G.es[G.get_eid(j,i)]["w"]
                    i["pred"] = j
        # affichage des résultats 
        str_names = ""
        str_dist = "\\texttt{dist} & "
        str_pred = "\\texttt{pred} &"
        for x in G.vs:
            str_names = str_names + x["name"] + '\t&'
            str_dist = str_dist + str(x["dist"]) + '\t&'
            if x["pred"] == "":
                str_pred = str_pred + '\t&'
            else:
                str_pred = str_pred + x["pred"]["name"] + '\t&'
        print(str_names)
        print(str_pred)
        print(str_dist)
        print('----------------------------------------------')

g = mygraphs.build_exemple_pcc()
print(g)
visual_style = {}
visual_style['edge_width'] = 2
visual_style['node_size'] = .8
visual_style['standalone'] = False
visual_style['node_opacity'] = 0.5
visual_style['vertex_label'] = g.vs["name"]
visual_style['edge_label'] = g.es["w"]
visual_style['canvas'] = (9,6)
layout = { 
    0: (-1,-1),
    1: (1,0),
    2: (1,-4),
    3: (2,-2),
    4: (3,-3),
    5: (5,0),
    6: (5,-3),
    7: (6,-4)
}
visual_style['layout'] = layout
plot(g,'ordinal-0.pdf',**visual_style)
ordinal(g,g.vs.find(name="s"))



