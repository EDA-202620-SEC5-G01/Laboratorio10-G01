from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as vr

def new_graph(order):
    return {
        "vertices": mp.new_map(num_elements=order, load_factor=0.5),
        "num_edges": 0
    }
 
 
def insert_vertex(my_graph, key_u, info_u):
    new_v = vr.new_vertex(key_u, info_u)
    mp.put(my_graph["vertices"], key_u, new_v)
    return my_graph
 
 
def add_edge(my_graph, key_u, key_v, weight=0):
    vertex_u = mp.get(my_graph["vertices"], key_u)
    if vertex_u is not None:
        vr.add_adjacent(vertex_u, key_v, weight)
        my_graph["num_edges"] += 1
    return my_graph
 
 
def contains_vertex(my_graph, key_u):
    return mp.get(my_graph["vertices"], key_u) is not None
 
 
def order(my_graph):
    return mp.size(my_graph["vertices"])
 
 
def size(my_graph):
    return my_graph["num_edges"]
 
 
def degree(my_graph, key_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is not None:
        return vr.degree(vertex)
    return 0
 
 
def adjacents(my_graph, key_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is not None:
        return vr.get_adjacents(vertex)
    return None
 
 
def vertices(my_graph):
    return mp.key_set(my_graph["vertices"])
 
 
def edges_vertex(my_graph, key_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is not None:
        return mp.value_set(vr.get_adjacents(vertex))
    return None
 
 
def get_vertex(my_graph, key_u):
    return mp.get(my_graph["vertices"], key_u)
 
 
def update_vertex_info(my_graph, key_u, info_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is not None:
        vr.set_value(vertex, info_u)
    return my_graph
 
 
def get_vertex_information(my_graph, key_u):
    vertex = mp.get(my_graph["vertices"], key_u)
    if vertex is not None:
        return vr.get_value(vertex)
    return None