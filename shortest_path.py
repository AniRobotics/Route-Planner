import heapq
import pickle
import networkx as nx
import matplotlib.pyplot as plt

# Load the graph
city_map = pickle.load(open("graph.p", "rb"))

# Define start and goal nodes
start_node, goal_node = "Arad", "Bucharest"

# ///////////////////  Start of Minimum-Cost-Path-Search ////////////////////////////
# this is a priority queue to hold (cost, node) pair
# where cost is the minimum cost to reach to node from start_node
frontier = list()

# holds nodes that have already been explored
explored_set = set()

# holds path nodes
path = list()

# holds minimum-cost parent-node
best_parent = dict()

# Add start node and its cost to the frontier list
heapq.heappush(frontier, (0, start_node))   # heappush the (min-cost, node) pair
best_parent[start_node] = None              # start node's parent is None

# Start exploring the map
goal_reached = False
min_path_cost = None
# while (len(frontier) > 0) and (not goal_reached):
while len(frontier) > 0:
    node_cost_pair = heapq.heappop(frontier)
    current_node = node_cost_pair[1]  # index 1 has the node name (value)
    explored_set.add(current_node)

    if current_node == goal_node:
        min_path_cost = node_cost_pair[0]
        goal_reached = True
        print("Goal node reached")

    # Check all the neighbors of the current node
    for neighbor in city_map.neighbors(current_node):
        cost_f = city_map[current_node][neighbor]["weight"] + node_cost_pair[0]

        # if this neighbor-node has already explored, then skip to next neighbor
        if neighbor in explored_set:
            continue

        # check if this neighbor-node is in the frontier nodes list
        exists_flag = False
        for index, element in enumerate(frontier):
            if element[1] == neighbor:
                exists_flag = True
                if element[0] > cost_f:
                    frontier[index][0] = cost_f
                    best_parent[neighbor] = current_node
                break

        if not exists_flag:
            heapq.heappush(frontier, (cost_f, neighbor))
            best_parent[neighbor] = current_node


# //////////////////////// Now extract the path /////////////////////////////
path.append(goal_node)
current_parent = best_parent[goal_node]
while not current_parent is None:
    path.append(current_parent)
    current_parent = best_parent[current_parent]
path.reverse()

# //////////////////// Print the path //////////////////////////////
print("Path nodes: ")
print(path)
print("Minimum path cost: %i"%min_path_cost)

# ////////////////////// Plot the graph ////////////////////////////
weight = nx.get_edge_attributes(city_map, "weight")
pos = nx.get_node_attributes(city_map, "pos")

path_edge_list = list()
for i in range(len(path)-1):
    path_edge_list.append((path[i], path[i+1]))
print(path_edge_list)

plt.figure()
nx.draw_networkx(city_map, pos, node_color=[1.0, 0.3, 0.0], node_size=1000, font_color=[0.0, 0.0, 1.0], node_shape="o", edge_color="k", linewidths=1)
nx.draw_networkx_edges(city_map, pos, edgelist=city_map.edges, edge_color="k", width=1)
# nx.draw_networkx_nodes(city_map, pos, nodelist=city_map.nodes)
nx.draw_networkx_edge_labels(city_map, pos, edge_labels=weight, font_color="m")

nx.draw_networkx_edges(city_map, pos, edgelist=path_edge_list, edge_color="g", width=4)

plt.axis('off')
plt.show()

# print(city_map.nodes)
# print(city_map.edges)
#
# print(city_map.nodes["Drobeta"])
# for i in city_map.neighbors("Drobeta"):
#     print(i)
#
# print(city_map["Drobeta"]["Mehadia"]["weight"])