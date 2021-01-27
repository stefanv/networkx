"""
==========
Javascript
==========

Example of writing JSON format graph data and using the D3 Javascript library
to produce an HTML/Javascript drawing.

The relevant JavaScript and HTMl can be found at:

https://github.com/networkx/networkx/tree/master/examples/external/force

"""
import json
import networkx as nx


G = nx.barbell_graph(6, 3)
# this d3 example uses the name attribute for the mouse-hover value,
# so add a name to each node
for n in G:
    G.nodes[n]["name"] = n


nx.drawing.display_d3js(G, js_path="force/force.js", html_path="force/force.html")
