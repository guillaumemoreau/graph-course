# algorithme de Bellmann 

import igraph as ig 
from network2tikz import plot
import mygraphs 
import math 
import numpy as np

def bellman(G,s):
    for i in G.vs:
        i["dist"] = math.inf
        i["pred"] = ""
        i["pred1"] = ""
    s["dist"] = 0
    for itr in range(0,len(G.vs)-1):
        print('Iteration '+str(itr))
        # recopie de dist et pred vers dist1 et pred1 
        for x in G.vs:
            x["dist1"] = x["dist"]
            x["pred1"] = x["pred"]
        for i in G.vs:
            # on recopie les valeurs précédentes 
            mcout = i["dist1"]
            msommet = i["pred1"]
            for j in i.predecessors():
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

def nb_latex(n):
    if n==float('inf'):
        return '+\infty'
    else:
        return str(n)

def export_latex_matrix(M):
    print('\\begin{pmatrix}')
    n = np.shape(M)[0]
    for i in range(0,n):
        for j in range(0,n):
            if j ==0:
                s = nb_latex(M[i, j])
            else:
                s = s + '& ' + nb_latex(M[i, j])
        s = s + '\\\\'
        print(s)
    print('\\end{pmatrix}')

def matrix_bellman(M):
    n = np.shape(M)[0]
    # mettre la diagonale à 0
    for i in range(0,n):
        M[i,i] = 0
    for m in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                #print(M[i,j])
                #print(M[i, m]+M[m, j])
                #print ('->')
                #print(min(M[i, j], M[i, m]+M[m, j]))
                M[i,j] = min (M[i,j],M[i,m]+M[m,j])
        export_latex_matrix(M)
        print('----')

