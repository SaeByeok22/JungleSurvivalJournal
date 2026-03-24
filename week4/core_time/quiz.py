graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'G': ['H'],
    'H': ['F'],
  }

def dfs(graph, start):
    visited = []
    back_edges = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph.get(node, []))
            for neighbor in graph.get(node, []):
                if neighbor in visited:
                    back_edges.add((node,neighbor))
        else:
            pass
        
    return visited, sorted(list(back_edges))