import networkx as nx
import matplotlib.pyplot as plt
import random


def add_unvisited_node(unvisited_nodes, edge):
    if edge[0] not in unvisited_nodes:
        unvisited_nodes.append(edge[0])
    if edge[1] not in unvisited_nodes:
        unvisited_nodes.append(edge[1])


def get_min_edge(min_edge, edge):
    if min_edge[2] > edge[2]:
        return edge
    else:
        return min_edge


def shortest_unbroken_path(edges):
    min_edge = edges[0]
    unvisited_nodes = []
    for edge in edges:
        min_edge = get_min_edge(min_edge, edge)
        add_unvisited_node(unvisited_nodes, edge)
    while unvisited_nodes:
        unvisited_nodes.pop()



if __name__ == '__main__':
    G = nx.Graph()
    n = 5
    nodes = range(n)
    edges = []
    weights = {}
    for i in range(n):
        for j in range(i + 1, n):
            if random.randint(0, 1) == 1:
                x = random.randint(1, 9)
                weights[(i, j)] = x
                edges.append((i, j, x))
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.show()

    shortest_unbroken_path(edges)
