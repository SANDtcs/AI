import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

 

class Graph:
 
    def __init__(self,vertices):
        self.V = vertices
        self.edges=[]
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        temp=[u,v]
        self.edges.append(temp)
        self.graph[u].append(v)
        
    def Visulaize(self):
        G=nx.Graph()
        edge_colours=['red']*10
        G.add_edges_from(self.edges)
        nx.draw_networkx(G,edge_color=edge_colours)
        plt.show()
        
    def printpath(self,src,target,maxDepth):
        path=[]
        edge=[]
        self.DLS(src,target,path,edge,maxDepth)

    def DLS(self,src,target,path,edge,maxDepth):
        
        path.append(src)
        
        if src == target : 
            print(path)
            print(edge)
            G1=nx.Graph()
            G1.add_edges_from(self.edges)
            edge_colours=['green' if list(e) in edge or [e[1],e[0]] in edge else 'red' for e in G1.edges]
            nx.draw_networkx(G1,edge_color=edge_colours)
            plt.show()
            
            return
        
        if maxDepth <=0 : 
            return

        for i in self.graph[src]:
                if(maxDepth>=0):
                    temp=[src,i]
                    edge.append(temp)
                    self.DLS(i,target,path,edge,maxDepth-1)
                    edge.pop()
                    
        path.pop()
        

g = Graph (6);
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 5)
g.addEdge(2, 4)
g.addEdge(4, 6)

g.Visulaize()
g.printpath(1, 6, 3)
