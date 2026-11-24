import math
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Stack import stack as st
from DataStructures.Graph import digraph as G
from DataStructures.Graph import edge as edg
from DataStructures.Graph import dijsktra_structure as ds
from DataStructures.List import array_list as al


def dijkstra(my_graph, source):
    estructura = ds.new_dijsktra_structure(source, G.order(my_graph))
    visitados = estructura["visited"]
    mp.put(visitados, source, {"marked": False, "edge_from": None, "dist_to": 0})
    pq.insert(estructura["pq"], 0, source)
    while not pq.is_empty(estructura["pq"]):
        v = pq.remove(estructura["pq"])
        info_v = mp.get(visitados, v)
        if not info_v["marked"]:
            info_v["marked"] = True
            arcos = G.edges_vertex(my_graph, v)
            for i in range(al.size(arcos)):
                arco = al.get_element(arcos, i)
                w = edg.to(arco)
                nueva_dist = info_v["dist_to"] + edg.weight(arco)
                info_w = mp.get(visitados, w)
                if info_w is None or nueva_dist < info_w["dist_to"]:
                    mp.put(visitados, w, {"marked": False, "edge_from": v, "dist_to": nueva_dist})
                    pq.insert(estructura["pq"], nueva_dist, w)
    return estructura


def dist_to(key_v, aux_structure):
    info = mp.get(aux_structure["visited"], key_v)
    if info is None:
        return math.inf
    return info["dist_to"]


def has_path_to(key_v, aux_structure):
    return mp.contains(aux_structure["visited"], key_v)


def path_to(key_v, aux_structure):
    if not has_path_to(key_v, aux_structure):
        return None
    camino = st.new_stack()
    actual = key_v
    while actual is not None:
        st.push(camino, actual)
        actual = mp.get(aux_structure["visited"], actual)["edge_from"]
    return camino
