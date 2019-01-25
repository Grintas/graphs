import graphmodule
import inputgen

"""
	This is an example demonstrating how graphmodule works
"""

#generate_matrices()
input_dir = 'data/'
f = open(input_dir+'D_undirected_weighted.txt','r')
m=[l.split(' ') for l in f.read().split('\n')]		# read adjecency matrix from file and save it in a two-dimensional list
f.close()

g=Graph(m)
print(g)
print(g.bfs('A'))		# breadth-first search algorithm finds the shortest paths from a given vertex to all other vertices, works for any graph.
print(g.bfs(4))
g.generate_matrix_of_distances()
g.vertices['A'].print_paths()
g.vertices[4].print_paths()

print(g.dfs())			# depth-first search algorithm generates a spanning tree if the given graph isn't directed

print(g.prim())			# prim's algorithm generates a minimal spanning tree of weighted undirected graph
