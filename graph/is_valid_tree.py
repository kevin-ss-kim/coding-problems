'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
'''


def is_valid_tree2(n, edges):
    if n == 1: return edges == []
    elif len(edges) + 1 == n:
        visited = set()
        adjacency_list = collections.defaultdict(list)
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
        queue = [edges[0][0]]
        search_from = None
        while len(queue):
            vertex = queue.pop(0)
            visited.add(vertex)
            for neighbor in adjacency_list[vertex]:
                if neighbor in visited:
                    if vertex in visited:
                        continue
                    elif search_from != neighbor:
                        return False
                else:
                    queue.append(neighbor)
            search_from = vertex
        return len(visited) == n
    return False


def is_valid_tree(n, edges):
    if len(edges) + 1 == n:
        visited = list()
        while len(edges):
            popped_edge = edges.pop()
            vertex1, vertex2 = popped_edge[0], popped_edge[1]
            neighbors = []
            visited.append(vertex1)
            for i, edge in enumerate(edges):
                if vertex1 == edge[0]:
                    vertex = edges.pop(i)[1]
                    if vertex in visited:
                        return False
                    neighbors.append(vertex)
                elif vertex1 == edge[1]:
                    vertex = edges.pop(i)[0]
                    if vertex in visited:
                        return False
                    neighbors.append(vertex)
            visited += neighbors
            neighbors = []
            visited.append(vertex2)
            for i, edge in enumerate(edges):
                if vertex2 == edge[0]:
                    vertex = edges.pop(i)[1]
                    if vertex in visited:
                        return False
                    neighbors.append(vertex)
                elif vertex2 == edge[1]:
                    vertex = edges.pop(i)[0]
                    if vertex in visited:
                        return False
                    neighbors.append(vertex)
            visited += neighbors
        return True
    return False
