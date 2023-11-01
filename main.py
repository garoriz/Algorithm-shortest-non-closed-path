import networkx as nx
import matplotlib.pyplot as plt
import random


def add_nodes_with_neighbors(edge):
    if edge[0] not in nodes_with_neighbors:
        nodes_with_neighbors.append(edge[0])
    if edge[1] not in nodes_with_neighbors:
        nodes_with_neighbors.append(edge[1])


def get_min_edge(min_edge, edge):
    if min_edge[2] > edge[2]:
        return edge
    else:
        return min_edge


def get_max_edge(max_edge, edge):
    if max_edge[2] < edge[2]:
        return edge
    else:
        return max_edge


def find_nearest_edge(visited_points):
    min_edge = (-1, -1, 10)
    for edge in edges:
        if edge[0] in visited_points and edge[1] in visited_points:
            continue
        if edge[0] in visited_points or edge[1] in visited_points:
            min_edge = get_min_edge(min_edge, edge)
    return min_edge


def draw_tree(G, node_arr, edge_arr, weight_arr):
    G.add_nodes_from(node_arr)
    G.add_weighted_edges_from(edge_arr)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_arr)
    plt.show()


def shortest_unbroken_path():
    min_edge = edges[0]
    for edge in edges:
        min_edge = get_min_edge(min_edge, edge)
    edges.remove(min_edge)
    min_edges.append(min_edge)
    visited_points = [min_edge[0], min_edge[1]]
    nodes_with_neighbors.remove(min_edge[0])
    nodes_with_neighbors.remove(min_edge[1])
    min_weights = {(min_edge[0], min_edge[1]): min_edge[2]}
    while nodes_with_neighbors:
        nearest_edge = find_nearest_edge(visited_points)
        min_edges.append(nearest_edge)
        if nearest_edge[0] not in visited_points:
            visited_points.append(nearest_edge[0])
        if nearest_edge[1] not in visited_points:
            visited_points.append(nearest_edge[1])
        if nearest_edge[0] in nodes_with_neighbors:
            nodes_with_neighbors.remove(nearest_edge[0])
        if nearest_edge[1] in nodes_with_neighbors:
            nodes_with_neighbors.remove(nearest_edge[1])
        edges.remove(nearest_edge)
        min_weights[(nearest_edge[0], nearest_edge[1])] = nearest_edge[2]

    draw_tree(nx.Graph(), visited_points, min_edges, min_weights)


def set_random_points():
    for i in range(n):
        for j in range(i + 1, n):
            if random.randint(0, 1) == 1:
                x = random.randint(1, 9)
                weights[(i, j)] = x
                edge = (i, j, x)
                edges.append(edge)
                add_nodes_with_neighbors(edge)


def delete_longest_edge():
    max_edge = (-1, -1, 0)
    for edge in min_edges:
        max_edge = get_max_edge(max_edge, edge)
    min_edges.remove(max_edge)
    weights.pop((max_edge[0], max_edge[1]))


def get_final_min_weights():
    min_weights = {}
    for edge in min_edges:
        min_weights[(edge[0], edge[1])] = edge[2]
    return min_weights


def set_neighbours_in_cluster(cluster, visited_nodes):
    for weight in final_min_weights:
        if weight[0] in cluster and weight[1] not in cluster:
            cluster.append(weight[1])
            visited_nodes.append(weight[1])
        if weight[1] in cluster and weight[0] not in cluster:
            cluster.append(weight[0])
            visited_nodes.append(weight[0])


def print_clusters():
    cluster_number = 1
    visited_nodes = []
    for node in nodes:
        cluster = []
        if node in visited_nodes:
            continue
        cluster.append(node)
        visited_nodes.append(node)
        set_neighbours_in_cluster(cluster, visited_nodes)
        print("cluster", cluster_number, ":", cluster)
        cluster_number += 1


if __name__ == '__main__':
    n = 10
    nodes = range(n)
    edges = []
    weights = {}
    nodes_with_neighbors = []
    while len(nodes_with_neighbors) != n:
        nodes_with_neighbors.clear()
        set_random_points()

    draw_tree(nx.Graph(), nodes, edges, weights)

    min_edges = []
    shortest_unbroken_path()

    k = 3

    while k > 0:
        delete_longest_edge()
        k -= 1

    final_min_weights = get_final_min_weights()
    draw_tree(nx.Graph(), nodes, min_edges, final_min_weights)
    print_clusters()
