# graphs
A simple graph module with a few algorithms.

Create a new graph using g = Graph(m), where m is an adjecency matrix given as a two dimensional list, for example, if

m = [['0', '1', '1', '0', '0', '0'],  
 ['1', '0', '0', '0', '0', '0'],  
 ['0', '1', '0', '0', '0', '0'],  
 ['0', '0', '0', '0', '1', '0'],  
 ['0', '0', '0', '1', '0', '0'],  
 ['0', '0', '0', '0', '1', '0']]  

then
g = Graph(m)

generates a graph, which you can print using
print(g)

this results in printing it's adjecency matrix:
\ A B C D E F  
A 0 1 1 0 0 0  
B 1 0 0 0 0 0  
C 0 1 0 0 0 0  
D 0 0 0 0 1 0  
E 0 0 0 1 0 0  
F 0 0 0 0 1 0  

given only one argument it automatically assigns letter names for all vertices, you can also specify another argument - a list of vertex names:

names = ['first', 'second', 'third', 'fourth', 'sixth']
print(Graph(m, names))
outputs the following:
\ first second third fourth fifth sixth
first 0 1 1 0 0 0
second 1 0 0 0 0 0
third 0 1 0 0 0 0
fourth 0 0 0 0 1 0
fifth 0 0 0 1 0 0
sixth 0 0 0 0 1 0


you can perform a breadth- first search on it using
g = Graph(m)  
g.bfs('A')  
or  
g.bfs(0)  

which results in the same - bfs returns a dictionary of shortest distances from vertex A to all other vertices:  
{0: 0, 1: 1, 2: 1, 3: '-', 4: '-', 5: '-', 'A': 0, 'B': 1, 'C': 1, 'D': '-', 'E': '-', 'F': '-'}  

as you can see you can refer to this dictionary both by vertex indices and assigned names (letters in this case)
BFS algorithm also generates all shortest paths from a given vertex and creates a vertex attribute - dictionary of all shortest paths. You can print them using vertex print_paths() method:  

g.vertices['A'].print_paths()  

which result in  
Shortest path from vertex A to vertex C is: A -> C  
Shortest path from vertex A to vertex B is: A -> B  

You can also generate all shortest paths using generate_matrix_of_distances() graph method:  

g.generate_matrix_of_distances()  

creates the mentioned paths dictionaries for all graph vertices and returns the matrix of distances:  
  A B C D E F  
A 0 1 1 - - -  
B 1 0 2 - - -  
C 2 1 0 - - -  
D - - - 0 1 -  
E - - - 1 0 -  
F - - - 2 1 0  

where '-' means inaccessible.  

besides bfs method there are two more:  
print(g.dfs())  
performs a depth-first search and returns a spanning tree graph object:  
\ A B C D E F  
A 0 0 0 0 0 0  
B 1 0 0 0 0 0  
C 0 1 0 0 0 0  
D 0 0 0 0 0 0  
E 0 0 0 1 0 0  
F 0 0 0 0 0 0  

g.prim() creates a minimal spanning tree for a weighted undirected graph.  
