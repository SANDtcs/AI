import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict


class Graphvisulaization:
   
    def __init__(self,vertices):
        self.edges=[]
        self.adj=defaultdict(list)
        self.vertices=vertices

       
    def addEdge(self,a,b):
        temp=[a,b]
        self.adj[a].append(b)
        self.edges.append(temp)

       
    def visualize(self):
        G=nx.Graph()
        edge_colours=['red']*10
        G.add_edges_from(self.edges)
        nx.draw_networkx(G,edge_color=edge_colours)
        plt.show()
 
       
    def printlist(self):
        print(self.edges)
        print(self.adj)

 

       
    def printpath(self,src,dest):
        visited=[False for i in range(self.vertices)]
        path=[]
        edge=[]
        self.printallpath(src,dest,visited,path,edge)


       
    def printallpath(self,src,dest,visited,path,edge):
        visited[src]=True
        path.append(src)
       
        if(src==dest):
            print(path)
            print(edge)
            G1=nx.Graph()
            G1.add_edges_from(self.edges)
            edge_colours=['green' if list(e) in edge or [e[1],e[0]] in edge else 'red' for e in G1.edges]
            nx.draw_networkx(G1,edge_color=edge_colours)
            plt.show()
     

        else:
            for i in self.adj[src]:
                if(visited[i]==False):
                    temp=[src,i]
                    edge.append(temp)
                    self.printallpath(i,dest,visited,path,edge)
                    edge.pop()
        path.pop()
        visited[src]=False
       


G=Graphvisulaization(6)
G.addEdge(0, 2)
G.addEdge(2, 1)
G.addEdge(0, 1)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(1, 0)
G.visualize()
#G.printlist()
G.printpath(0,4)
