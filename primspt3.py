from queue import PriorityQueue

def prim(graph):
    mst = []  
    visited = set() 
    pq = PriorityQueue() 
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)
    for neighbor, weight in graph[start_vertex]:
        pq.put((weight, start_vertex, neighbor))
    while len(visited) < len(graph):
        weight, u, v = pq.get()  
        if v not in visited:
            mst.append((u, v, weight))
            visited.add(v)
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    pq.put((weight, v, neighbor))
    return mst

graph = {
    'A': [('B', 3), ('C', 1)],
    'B': [('A', 3), ('C', 3), ('D', 6)],
    'C': [('A', 1), ('B', 3), ('D', 1)],
    'D': [('B', 6), ('C', 1)]
}

minimum_spanning_tree = prim(graph)

for u, v, weight in minimum_spanning_tree:
    print(f'{u} -- {v}  weight: {weight}')
