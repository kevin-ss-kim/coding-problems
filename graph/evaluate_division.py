'''
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].
'''


import collections

def find_path_product(start, end, visited, product, adjacency_list):
    if start not in adjacency_list or end not in adjacency_list:
        return -1.0
    elif start == end:
        return product
    for neighbor in adjacency_list[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            calc_product = find_path_product(neighbor, end, visited, product * adjacency_list[start][neighbor], adjacency_list)
            if calc_product != -1.0:
                return calc_product
    return -1.0

def evaluate_division(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    result = []
    adjacency_list = collections.defaultdict(dict)
    # Make graph
    for i in range(len(equations)):
        adjacency_list[equations[i][0]][equations[i][1]] = values[i]
        adjacency_list[equations[i][1]][equations[i][0]] = 1 / values[i]
    for query in queries:
        visited = set()
        visited.add(query[0])
        result.append(find_path_product(query[0], query[1], visited, 1.0, adjacency_list))
    return result
