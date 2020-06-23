# algorithme de Bellmann 

import igraph as ig 
from network2tikz import plot
import mygraphs 
import math 


def bellmann(G,s):
    for i in G.vs:
        i["dist"] = math.inf
        i["pred"] = ""
        i["pred1"] = ""
    s["dist"] = 0
    for itr in range(0,len(G.vs)-1):
        # recopie de dist et pred vers dist1 et pred1 
        for x in G.vs:
            x["dist1"] = x["dist"]
            x["pred1"] = x["pred"]
        for i in G.vs:
            mcout = i["dist1"]
            msommet = x["pred1"]
            for j in i.predecessors():
                    print('('+i["name"]+','+j["name"]+') : ')
                    if j["dist"]+G.es[G.get_eid(j,i)]["w"] < i["dist"]:
                        mcout = j["dist"]+G.es[G.get_eid(j,i)]["w"]
                        msommet = j
            i["dist1"] = mcout 
            i["pred1"] = msommet 
        # affichage des résultats 
        str_names = " & "
        str_dist = "\\texttt{dist} & "
        str_pred = "\\texttt{pred} &"
        for x in G.vs:
            str_names = str_names + x["name"] + '\t&'
            str_dist = str_dist + str(x["dist1"]) + '\t&'
            if x["pred1"] == "":
                str_pred = str_pred + '\t&'
            else:
                str_pred = str_pred + x["pred1"]["name"] + '\t&'
        print(str_names)
        print('\hline')
        print(str_pred)
        print(str_dist)
        print('----------------------------------------------')
        # on recopie dist1 et pred1 dans dist0 et pred0 
        for x in G.vs:
            x["dist"] = x["dist1"]
            x["pred"] = x["pred1"]

g = mygraphs.build_exemple_bellmann()
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
    0: (-1,0),
    1: (2,1),
    2: (2,-1),
    3: (4,0),
    4: (3,-3),
    5: (6,-1),
}
visual_style['layout'] = layout
plot(g,'bellmann-0.pdf',**visual_style)
bellmann(g,g.vs.find(name="1"))
