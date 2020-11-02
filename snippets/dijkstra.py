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



