import networkx as nx
import heapq
from math import ceil
from numpy import inf

# from InstanceGenerator import InstanceGenerator

class Node:
    def __init__(self, lb, level, cost, solution) -> None:
        self.lb = lb
        self.level = level
        self.cost = cost
        self.sol = solution

class BranchAndBoundTSP:

    def findMinWeights(self, nodeEdges):
        print(nodeEdges)
        for pos in range(2):
            minValue = nodeEdges[pos]
            newPosition = pos
            for i in range(pos, len(nodeEdges)):
                if minValue[2]['weight'] > nodeEdges[i][2]['weight']:
                    minValue = nodeEdges[i]
                    newPosition = i
            aux = nodeEdges[pos]
            nodeEdges[pos] = minValue
            nodeEdges[newPosition] = aux
        print(nodeEdges)
        print('=========================')
        return nodeEdges
    
    def initRoot(self, graph):
        lb = 0
        for node in graph:
            nodeEdges = list(graph.edges(node, data=True))
            nodeEdges = self.findMinWeights(nodeEdges)
            lb += nodeEdges[0][2]['weight'] + nodeEdges[1][2]['weight']
        lb = ceil(lb / 2)
        print(lb)
        root = Node(lb, 0, 0, [list(graph.nodes)[0]])
        return root
    
    def bound(self, solution, newNode, graph):
        lb = 0
        for n in graph:
            nodeEdges = list(graph.edges(n, data=True))
            nodeEdges.sort(key=lambda t: t[2]['weight'])
            if n != newNode and n != solution[-1]:
                lb += nodeEdges[0][2]['weight'] + nodeEdges[1][2]['weight']
            else:
                lb += nodeEdges[0][2]['weight'] + nodeEdges[1][2]['weight']
        lb = ceil(lb / 2)

    """
    def BnB(self, graph, root):
        num_nodes = len(graph.nodes())
        queue = []
        heapq.heappush(queue, root)
        best = inf
        while queue:
            node = heapq.heappop(queue)
            if node.level > num_nodes - 1:
                if best > node.cost:
                    best = node.cost
                    solution = node.sol
            elif node.lb < best:
                if node.level < num_nodes - 1:
                for vertex in graph:
                    newBound = self.bound(node.solution, vertex, graph)
                    if not vertex in node.solution and node != vertex and newBound < best:
                        heapq.heappush(queue, vertex)
    """

    def runBranchAndBound(self, graph):
        root = self.initRoot(graph)
        #self.BnB(graph, root)

    
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


BnB = BranchAndBoundTSP()
BnB.runBranchAndBound(G)
for node in G:
    nodeEdges = list(G.edges(node, data=True))
    BnB.findMinWeights(nodeEdges)
