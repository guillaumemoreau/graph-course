# algorithme de Diskstra 

import igraph as ig 
from network2tikz import plot
import mygraphs 
import math 


def dijkstra(G,s):
    for i in G.vs:
        i["dist"] = math.inf
        i["pred"] = ""
        i["done"] = False 
    s["dist"] = 0
    pas_fini = True 
    while pas_fini:
        mcout = math.inf
        msommet = s 
        for i in G.vs:
            if i["done"] == False:
                if (i["dist"] < mcout):
                    mcout = i["dist"]
                    msommet = i 
        if (mcout < math.inf):
            msommet["done"] = True 
            for j in msommet.successors():
                if msommet["dist"]+G.es[G.get_eid(msommet,j)]["w"] < j["dist"]:
                    j["dist"] = msommet["dist"]+G.es[G.get_eid(msommet,j)]["w"]
                    j["pred"] = msommet
        else:
            pas_fini = False 
        # affichage des résultats 
        str_names = " & "
        str_dist = "\\texttt{dist} & "
        str_pred = "\\texttt{pred} &"
        for x in G.vs:
            if x["done"]:
                str_names = str_names + '\\textbf{' + x["name"] + '}\t&'
            else:
                str_names = str_names + x["name"] + '\t&'
            str_dist = str_dist + str(x["dist"]) + '\t&'
            if x["pred"] == "":
                str_pred = str_pred + '\t&'
            else:
                str_pred = str_pred + x["pred"]["name"] + '\t&'
        print(str_names)
        print('\hline')
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
plot(g,'dijkstra-0.pdf',**visual_style)
dijkstra(g,g.vs.find(name="s"))
