import igraph as ig
from network2tikz import plot

import mygraphs

astar = {}

def visite(l,i):
    global astar 
    global gstar 
    print('entering visite('+str(l)+','+str(i)+')')
    astar[l,i] = True 
    if (~gstar[l,i]):
        gstar[l,i] = 1
    for j in gstar.successors(i):
        print('on essaie '+str(l)+','+str(j))
        if l == j:
            print("auto")
        else:
            if astar[l,j] == False:
                visite(l,j)

def fermeture_transitive(g):
    global astar
    for e1 in gstar.vs:
        for e2 in gstar.vs:
            astar[e1.index,e2.index] = False
    for i in gstar.vs:
        visite(i.index,i.index)

g1, visual_style = mygraphs.build_graph_exemple_6()
plot(g1,"ft0.tex",**visual_style)
gstar = g1.copy()
fermeture_transitive(g1)
plot(gstar, "ft1.tex", **visual_style)
