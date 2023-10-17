import networkx as nx
import matplotlib.pyplot as plt
import random


def add_nodes_with_neighbors(nodes_with_neighbors, edge):
    if edge[0] not in nodes_with_neighbors:
        nodes_with_neighbors.append(edge[0])
    if edge[1] not in nodes_with_neighbors:
        nodes_with_neighbors.append(edge[1])


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
        add_nodes_with_neighbors(unvisited_nodes, edge)
    while unvisited_nodes:
        unvisited_nodes.pop()


def set_random_points():
    for i in range(n):
        for j in range(i + 1, n):
            if random.randint(0, 1) == 1:
                x = random.randint(1, 9)
                weights[(i, j)] = x
                edge = (i, j, x)
                edges.append(edge)
                add_nodes_with_neighbors(nodes_with_neighbors, edge)


if __name__ == '__main__':
    G = nx.Graph()
    n = 5
    nodes = range(n)
    edges = []
    weights = {}
    nodes_with_neighbors = []
    while len(nodes_with_neighbors) != n:
        nodes_with_neighbors.clear()
        set_random_points()

    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.show()

    shortest_unbroken_path(edges)
