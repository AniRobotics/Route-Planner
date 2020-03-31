import networkx as nx
import matplotlib.pyplot as plt
# from helpers import Map, load_map, show_map

# instantiate the graph object
G = nx.Graph()

# Create nodes to the graph with positions in the plot
G.add_node("Drobeta", pos=(0, 0))
G.add_node("Mehadia", pos=(-0.5, 0.5))
G.add_node("Lugoj", pos=(0, 1.0))
G.add_node("Timisoara", pos=(-1, 1))
G.add_node("Arad", pos=(-0.5, 2.0))
G.add_node("Zerind", pos=(-1, 2.5))
G.add_node("Oradea", pos=(-0.5, 3.0))
G.add_node("Craiova", pos=(1, 0))
G.add_node("Rimnicu Vilcea", pos=(1.0, 1.5))
G.add_node("Sibiu", pos=(0.5, 2.5))
G.add_node("Pitesti", pos=(1.5, 1.0))
G.add_node("Fagaras", pos=(1.5, 2.5))
G.add_node("Giurgiu", pos=(2.0, 0.5))
G.add_node("Bucharest", pos=(2.5, 1.5))
G.add_node("Urziceni", pos=(3.5, 2.0))
G.add_node("Eforie", pos=(3.0, 0.5))
G.add_node("Hirsova", pos=(4.0, 1.0))
G.add_node("Vaslui", pos=(4.0, 3.0))
G.add_node("Iasi", pos=(3.0, 2.5))
G.add_node("Neamt", pos=(2.5, 3.0))

# Create edges with "weight" as attribute
G.add_edge("Drobeta", "Mehadia", weight=75)
G.add_edge("Drobeta", "Craiova", weight=120)
G.add_edge("Mehadia", "Lugoj", weight=70)
G.add_edge("Lugoj", "Timisoara", weight=111)
G.add_edge("Timisoara", "Arad", weight=118)
G.add_edge("Arad", "Zerind", weight=75)
G.add_edge("Arad", "Sibiu", weight=140)
G.add_edge("Zerind", "Oradea", weight=71)
G.add_edge("Oradea", "Sibiu", weight=151)
G.add_edge("Sibiu", "Fagaras", weight=99)
G.add_edge("Sibiu", "Rimnicu Vilcea", weight=80)
G.add_edge("Rimnicu Vilcea", "Pitesti", weight=97)
G.add_edge("Rimnicu Vilcea", "Craiova", weight=146)
G.add_edge("Craiova", "Pitesti", weight=138)
G.add_edge("Fagaras", "Bucharest", weight=211)
G.add_edge("Bucharest", "Urziceni", weight=85)
G.add_edge("Bucharest", "Giurgiu", weight=90)
G.add_edge("Urziceni", "Hirsova", weight=98)
G.add_edge("Urziceni", "Vaslui", weight=142)
G.add_edge("Hirsova", "Eforie", weight=86)
G.add_edge("Vaslui", "Iasi", weight=92)
G.add_edge("Iasi", "Neamt", weight=87)

# Plot the graph
weight = nx.get_edge_attributes(G, "weight")
pos = nx.get_node_attributes(G, "pos")

plt.figure()
nx.draw_networkx(G, pos, node_color=[1.0, 0.3, 0.0], node_size=1000, font_color=[0.1, 0.0, 1.0], node_shape="o", edge_color="k", linewidths=1)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight, font_color=[1.0, 0.1, 0.5])
plt.axis('off')
plt.show()


##########################################################################################################
# city_names = ["Drobeta", "Mehadia", "Lugoj", "Timisoara", "Arad", "Zerind", "Oradea", "Craiova",
#               "Rimnicu Vilcea", "Sibiu", "Pitesti", "Fagaras", "Giurgiu", "Bucharest", "Urziceni", "Eforie",
#               "Hirsova", "Vaslui", "Iasi", "Neamt"]
# G.add_nodes_from(city_names)

# # Create edges with "weight" as attribute
# edges = list()
# edges.append(("Drobeta", "Mehadia", {"weight": 75}))
# edges.append(("Drobeta", "Craiova", {"weight": 120}))
# edges.append(("Mehadia", "Lugoj", {"weight": 70}))
# edges.append(("Lugoj", "Timisoara", {"weight": 111}))
# edges.append(("Timisoara", "Arad", {"weight": 118}))
# edges.append(("Arad", "Zerind", {"weight": 75}))
# edges.append(("Arad", "Sibiu", {"weight": 140}))
# edges.append(("Zerind", "Oradea", {"weight": 71}))
# edges.append(("Oradea", "Sibiu", {"weight": 151}))
# edges.append(("Sibiu", "Fagaras", {"weight": 99}))
# edges.append(("Sibiu", "Rimnicu Vilcea", {"weight": 80}))
# edges.append(("Rimnicu Vilcea", "Pitesti", {"weight": 97}))
# edges.append(("Rimnicu Vilcea", "Criova", {"weight": 146}))
# edges.append(("Criova", "Pitesti", {"weight": 138}))
# edges.append(("Fagaras", "Bucharest", {"weight": 211}))
# edges.append(("Bucharest", "Urziceni", {"weight": 85}))
# edges.append(("Bucharest", "Giurgiu", {"weight": 90}))
# edges.append(("Urziceni", "Hirsova", {"weight": 98}))
# edges.append(("Urziceni", "Vaslui", {"weight": 142}))
# edges.append(("Hirsova", "Eforie", {"weight": 86}))
# edges.append(("Vaslui", "Iasi", {"weight": 92}))
# edges.append(("Iasi", "Neamt", {"weight": 87}))
