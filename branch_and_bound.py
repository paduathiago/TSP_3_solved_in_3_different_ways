import networkx as nx

# from InstanceGenerator import InstanceGenerator

class BranchAndBoundTSP:

    def initRoot(self, graph):
        weightSum = 0
        for node in graph:
            nodeEdges = list(graph.edges(node, data=True))
            nodeEdges.sort(key=lambda t: t[2]['weight'])
            weightSum += nodeEdges[0][2]['weight'] + nodeEdges[1][2]['weight']
        return weightSum/2
            
    
G = nx.Graph()
G.add_edge('a', 'b', weight=3)
G.add_edge('a', 'c', weight=1)
G.add_edge('a', 'e', weight=8)
G.add_edge('a', 'd', weight=5)
G.add_edge('b', 'c', weight=6)
G.add_edge('b', 'd', weight=7)
G.add_edge('b', 'e', weight=9)
G.add_edge('c', 'd', weight=4)
G.add_edge('c', 'e', weight=2)
G.add_edge('d', 'e', weight=3)

print(G['a']['b']['weight'])


BnB = BranchAndBoundTSP()
BnB.initRoot(G)
