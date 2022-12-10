import networkx as nx
import heapq
from math import ceil
from copy import deepcopy
from numpy import inf

# from InstanceGenerator import InstanceGenerator

class Node:
    def __init__(self, lb, level, cost, solution) -> None:
        self.lb = lb
        self.level = level
        self.cost = cost
        self.sol = solution

    def __gt__(self, node2):
        if(self.lb > node2.lb):
            return True
        return False

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
    
    def findMinUsefulWeight(self, graph, solution):
        minWeight = inf
        for n in graph:
            for nbr in graph[n]:
                if graph[n][nbr]['weight'] < minWeight and graph[n] not in solution and graph[n] not in solution:
                    minWeight = graph[n][nbr]['weight']

        """
        for i in range(len(nodeEdges)):
            for j in range(len(nodeEdges)):
                if nodeEdges[i][j]['weight'] < minWeight and nodeEdges[i] not in solution and nodeEdges[i] not in solution:
                    minWeight = nodeEdges[i][j]['weight']
        """
        return minWeight
        

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
        auxSolution = deepcopy(solution)
        auxSolution.append(newNode)
        lb = 0
        nodes = list(graph.nodes)
        for i in range(len(nodes)):
            nodeEdges = list(graph.edges(nodes[i], data=True))
            if not nodes[i] in auxSolution:
                nodeEdges = self.findMinWeights(nodeEdges)
                lb += nodeEdges[0][2]['weight'] + nodeEdges[1][2]['weight']
            else:
                if i == 0 or i == len(nodes):
                    minWeight = self.findMinUsefulWeight(graph, auxSolution)
                    lb += minWeight
                    lb += graph[nodes[i]][nodes[i + 1]]['weight']
                else:
                    lb += graph[nodes[i]][nodes[i - 1]]['weight']
                    lb += graph[nodes[i]][nodes[i + 1]]['weight']
        
        lb = ceil(lb / 2)
        return lb

    
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
                        newBound = self.bound(node.sol, vertex, graph)
                        if not vertex in node.sol and node != vertex and newBound < best:
                            nextNode = Node(newBound, node.level + 1, node.cost + graph[node.sol[-1]][vertex]['weight'], node.sol.append(vertex))
                            heapq.heappush(queue, nextNode)
                elif graph[node.sol[-1]][0] != None and self.bound(node.sol, node.sol[0], graph) and len(node.sol) == len(graph.nodes):
                    nextNode = Node(newBound, node.level + 1, node.cost + graph[node.sol[-1]][node.sol[0]]['weight'], node.sol.append(node.sol[0]))
                    heapq.heappush(queue, nextNode)
    

    def runBranchAndBound(self, graph):
        root = self.initRoot(graph)
        self.BnB(graph, root)

    
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
