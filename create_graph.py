import csv
import random

import networkx as nx

# CSV schema: USERNAME,GROUP_RECV,FROM_GEO,GROUP_SEND,TO_GEO, ADDRESS
# Create all nodes in a directed graph in networkx from the csv file
# Each row in the csv file represents a node in the graph
def create_nodes_from_csv(csv_file):
  G = nx.DiGraph()
  with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    # Skip header
    next(reader)
    rows = []
    for row in reader:
      rows.append(row)
      # Add node to graph
    random.shuffle(rows)

    for row in rows:
        G.add_node(row[0],
                   recv=[i.strip() for i in row[1].split(',')],
                   src=row[2],
                   send=[i.strip() for i in row[3].split(',')],
                   to=[i.strip() for i in row[4].split(',')],
                   address=[i.strip() for i in row[5].split(',')])
    return G

# Check if any elements in send are present in recv
def send_recv_intersection(recv, send):
  return set(send).intersection(recv)

def can_send_geo(from_geo, to_geo):
  return from_geo in to_geo

# Create edges between nodes in the graph
def create_edges(G):
  for node in G.nodes():
    # Check if node can send to any other node
    for other_node in G.nodes():
      if node != other_node:
        # Check if node can send to other_node
        compatible_groups = send_recv_intersection(G.nodes[node]['send'], G.nodes[other_node]['recv'])
        if len(compatible_groups) > 0 and can_send_geo(G.nodes[other_node]['src'], G.nodes[node]['to']):
          G.add_edge(node, other_node, groups=compatible_groups,
                     src=G.nodes[node]['src'],
                     dest=G.nodes[other_node]['src'],
                     dest_groups=G.nodes[other_node]['recv'])
  return G

def is_hamiltonian_path(G, path):
    # Check if all edges in the proposed path exist
    return all(G.has_edge(path[i], path[i+1]) for i in range(len(path)-1))

def find_hamiltonian_path(G, current_path, remaining_nodes):
    # If there are no remaining nodes and the path is valid return the path
    if not remaining_nodes and is_hamiltonian_path(G, current_path):
        return current_path
    
    for node in list(remaining_nodes):
        # Try to extend the path by one node
        new_path = current_path + [node]
        # Proceed to next if the link between last node and current node exists.
        if G.has_edge(current_path[-1], node):
            new_remaining_nodes = set(remaining_nodes)
            new_remaining_nodes.remove(node)
            result = find_hamiltonian_path(G, new_path, new_remaining_nodes)
            # If a Hamiltonian path has been found, return the result
            if result:
                return result
    # If no path found return None
    return None

def get_hamiltonian_path(G):
    # Try every starting node, to find a Hamiltonian path
    for start_node in G.nodes():
        path = find_hamiltonian_path(G, [start_node], set(G.nodes()) - {start_node})
        if path:
            return path
    return None