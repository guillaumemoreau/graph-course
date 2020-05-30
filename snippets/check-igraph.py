# running igraph native tests for install check


import igraph as ig 
from network2tikz import plot

print (ig.__version__)

g = ig.Graph.Famous("petersen")
ig.plot(g)
# also check tikz export
plot(g,'test.tex')
