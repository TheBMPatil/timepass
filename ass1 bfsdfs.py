class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex)

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = []
        queue.append(start)
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

print("DFS:")
g.dfs('A')

print("BFS:")
g.bfs('A')
