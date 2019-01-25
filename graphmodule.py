class Vertex():
    def __init__(self, id, name=''):
        self.id = id
        self.name = name
        self.adj_list = []      # adjecency list
        self.color = 'white'    # color represents one of the three possible states for a vertex: white - not yet visited; gray - visited, but not analyzed (might be revisited); black - visited and analyzed (will not be revisited)
        self.distances = {}     # dictionary of distances to other vertices, keys are id's
        self.paths = {}         # dictionary of shortest paths to other vertices
        self.parent = None
        # print(self.name)
        # self.start_time = 0
        # self.end_time = 0
        # self.descendants=[]     
    
    def __str__(self):
        if self.name != '':
            return str(self.name)
        else:
            return str(self.id)
    # @property
    # def name(self):
    #     if self.name != '':
    #         return self.name
    #     else:
    #         return self.id
    
    def print_attributes(self):
        print('          id =', self.id, '\n          name =', self.name, '\n          color =',self.color, '\n          distances =',self.distances, '\n          parent =',self.parent)
    
    def print_paths(self, names=True):
        for k in self.paths.keys():
            if names:
                if not str(k).isdigit():
                    print('Shortest path from vertex',self.name,'to vertex',self.paths[k][-1].name,'is: ',end='')
                    print(' -> '.join([v.name for v in self.paths[k]]))
            else:
                if str(k).isdigit():
                    print('Shortest path from vertex',self.id,'to vertex',self.paths[k][-1].id,'is: ',end='')
                    print(' -> '.join([str(v.id) for v in self.paths[k]]))
        print()
        
class Edge():
    def __init__(self,u,v, w=1):
        self.u = u    # start vertex
        self.v = v    # end vertex
        self.w = w    # weight of the edge
    
    def __str__(self):
        return str(self.u.name) + ' --' + str(self.w) + '--> ' + str(self.v.name)
        
class Graph():
    """ Graph is initialized given a mandatory argument adjecency matrix and an optional argument names, for naming graph nodes.
        If no names argument provided, alphabetical naming of vertices will be automatically generated
    """
    def __init__(self, adj_matrix, names=None):
        self.adj_matrix = adj_matrix
        if names is None:
            names=[chr(x) for x in range(65, 65+len(adj_matrix))]
        self.names=names
        # print(self.names)
        self.n = len(adj_matrix)    # number of vertices in the graph
        self.vertices = {}          # dictionary of vertices: keys are either id's or names, values are Vertex objects
        self.edges = []
        for i in range(self.n):     # initializing dictionary of vertices
            v = Vertex(i,names[i])
            self.vertices[names[i]]=v
            self.vertices[i]=v
        for i in range(self.n):     # initializing dictionary of edges and vertex adjecency lists
            for j in range(self.n):
                if adj_matrix[i][j] != '0':
                    self.edges.append(Edge(self.vertices[i],self.vertices[j],int(adj_matrix[i][j])))
                    self.vertices[i].adj_list.append(self.vertices[j])
        self.m = len(self.edges)    # number of edges in the graph
        self.directed = not all(self.adj_matrix[i][i]==self.adj_matrix[j][j] for i in range(self.n) for j in range(self.n)) # if adj_matrix is symmetrical - the graph is undirected
        self.weighted = all(e.w == 1 for e in self.edges)
        self.total_graph_weight = sum(e.w for e in self.edges)

    def __str__(self):
        me = '\n'.join([self.names[i]+' '+' '.join(a) for i,a in enumerate(self.adj_matrix)])
        me = '\ '+' '.join(self.names) + '\n' + me
        return me
        
    def reinitialize_vertices(self):
        for v in set(self.vertices.values()):
            v.color='white'
            v.parent=None
    
    def gen_spanning_tree(self):    
        spanning_tree_matrix=[['0' for i in range(self.n)] for j in range(self.n)]
        spanning_tree_edges=[]
        for u in set(self.vertices.values()):
            # print(u.name)
            if u.parent is not None:
                print('adding edge', Edge(u.parent, u, int(self.adj_matrix[u.parent.id][u.id])))
                spanning_tree_edges.append(Edge(u.parent, u, int(self.adj_matrix[u.parent.id][u.id])))
        for u in set(self.vertices.values()):
            for edge in spanning_tree_edges:
                if u == edge.u:
                    spanning_tree_matrix[u.id][edge.v.id] = self.adj_matrix[u.id][edge.v.id]
        return Graph(spanning_tree_matrix)

    def bfs(self, root):
        """ Breadth First Search:
            Given a source vertex 'root' of the graph does the following:
                sets self.vertices[root].distances to a dictionary of distances to other accessible from root vertices: root.distances[u] = shortest distance between vertices root and u
                sets self.vertices[root].paths to a dictionary of shortest paths to other vertices, accessible from root: root.paths[u] = a list of vertices on the shortest path from root to u
                returns root.distances dictionary
        """
        # Might add the following features: default root to set(self.vertices), then given no root argument perform bfs on all vertices (just like generate_matrix_of_distances() does).
        # Also would be useful to take a search node and terminate algorithm once it's found.
        root=self.vertices[root]
        print("Starting breadth-first search algorithm for vertex:",root,'\n')
        root.color='gray'
        root.distances={v:'-' for v in range(self.n)}
        root.distances[root.id]=0
        q=[self.vertices[root.id]]
        while q != []:
            u=q[0]
            print('Queue Q is now',[v.name for v in q],'\nstarting to analyze vertex', u, '\n' + str(u.name) + '.adj_list =', [v.name for v in u.adj_list], '\n')
            for v in u.adj_list:
                print('        Analyzing vertex', v.name)
                if v.color=='white':
                    v.color='gray'
                    root.distances[v.id]=root.distances[u.id]+1
                    v.parent=u
                    q.append(v)
                # print('          ', end='')
                v.print_attributes()
                print('        root.distances =',root.distances)
                print()
            q.remove(u)
            u.color='black'
        distances = root.distances
        if self.names != []:
            distances.update(dict(zip(self.names,[distances[i] for i in range(self.n)])))
        for v in set(self.vertices.values()):
            if v.parent is not None:
                shortest_path=[v]
                p=v.parent
                while p is not None:
                    shortest_path.append(p)
                    p=p.parent
                shortest_path = shortest_path[::-1]
                root.paths[v.id] = shortest_path
                root.paths[v.name] = shortest_path
        self.reinitialize_vertices()
        return distances
    
    def generate_matrix_of_distances(self):
        """ Calls bfs() for all vertices of the graph, prints and returns the distance matrix
        """
        for i in range(self.n):
            self.bfs(i)
        matrix = " ".join(self.names).rjust(len(self.names)*2+1,' ')
        for i in range(self.n):
            matrix += '\n'+self.names[i]+ ' ' + ' '.join([str(self.vertices[i].distances[j]) for j in range(self.n) if j in self.vertices[i].distances.keys()])
        print(matrix)
        self.distance_matrix=[[self.vertices[i].distances[j] for j in range(self.n)] for i in range(self.n)]
        self.reinitialize_vertices()
        return self.distance_matrix
        
    def dfs(self,root=None):
        """ Depth first search: for undirected graph generates a spanning tree and creates a graph attribute spanning_tree_matrix = incidence matrix of the spanning tree
                for a directed graph, given a root vertex, generates a successor tree for that vertex (yet to be implemented)
        """
        if self.directed:
            if root is not None:
                print('Graph is directed, therefore spanning tree will not be created.') # 'DFS algorithm will produce a succesor tree for given vertex:', root)    # not yet implemented
        else:
            print('Graph is undirected, starting DFS algorithm')

        time = 0                                    # start of recursive DFS algorithm
        def visit(u):
            print('Visiting', u)
            print(u, '.adj_list =',[v.name for v in u.adj_list])
            u.color='gray'
            nonlocal time
            time += 1
            u.start_time = time
            print('u.start_time =', u.start_time)
            for v in u.adj_list:
                if v.color=="white":
                    v.parent=u
                    print(v.name,'parent is',u.name)
                    visit(v)
            u.color='black'
            time += 1
            u.end_time=time
            print('u.end_time =', u.end_time)
        for u in set(self.vertices.values()):
            if u.color=='white':
                visit(u)                            # end of DFS algorithm
        if not self.directed:                       # if graph is undirected, generate a spanning tree
            self.spanning_tree = self.gen_spanning_tree()
            # print(self.spanning_tree)
            self.reinitialize_vertices()
            return self.spanning_tree
        
    def prim(self):
        """ Returns minimal spanning tree of a weighted undirected graph
        """
        if self.directed:
            return None
        q = list(set(self.vertices.values())) # queue of vertices to visit
        for v in q:
            v.key=float("inf")
        root=q[0]   # can be arbitrary vertex, since all of them will have to be visited anyway
        root.key=0
        while q != []:
            print('Queue Q is now',[v.name for v in q])
            min_key = min([v.key for v in q])
            print('min_key =', min_key)
            u = [v for v in q if v.key == min_key][0]
            q.remove(u)
            print('starting to analyze ', u, 'with adj_list =', [v.name for v in u.adj_list])
            for v in u.adj_list:
                if v in q and int(self.adj_matrix[u.id][v.id]) < v.key:
                    print(v, 'is still in Q and', v.name + '.key = ',v.key, '=>\n    parent = {}\n    key = {}'.format(u.name, self.adj_matrix[u.id][v.id]))
                    v.parent = u
                    v.key = int(self.adj_matrix[u.id][v.id])
        self.minimal_spanning_tree = self.gen_spanning_tree()
        # print(self.minimal_spanning_tree)
        self.reinitialize_vertices()
        return self.minimal_spanning_tree
