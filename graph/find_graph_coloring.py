# Given an undirected graph with maximum degree D, find a graph coloring using at most D+1 colors.

class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')

a.neighbors.add(b)
a.neighbors.add(c)
a.neighbors.add(d)
a.neighbors.add(e)
b.neighbors.add(a)
b.neighbors.add(c)
b.neighbors.add(d)
b.neighbors.add(e)
c.neighbors.add(a)
c.neighbors.add(b)
c.neighbors.add(d)
c.neighbors.add(e)
d.neighbors.add(a)
d.neighbors.add(b)
d.neighbors.add(c)
d.neighbors.add(e)
e.neighbors.add(a)
e.neighbors.add(b)
e.neighbors.add(c)
e.neighbors.add(d)

graph = [a, b, c, d, e]

def color_graph(graph, colors):
    for node in graph:
        # A node with a loop is adjacent to itself so it can't have the same color as itself
        if node in node.neighbors:
            raise Exception('Loop detected in graph. Impossible to color')
        # Get the neighbor's colors
        illegal_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])
        # Assign the first legal color
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break
        # Get a list of legal colors and assign first color (slower)
        # legal_colors = [color for color in colors if color not in illegal_colors]
        # node.color = legal_colors[0]
        print(node.label + ': ' + node.color)

def main():
    colors = ['Red', 'Green', 'Blue', 'Black', 'White']
    color_graph(graph, colors)

main()