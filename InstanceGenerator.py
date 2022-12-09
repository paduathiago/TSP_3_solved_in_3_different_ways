import networkx as nx

from point import Point
from random import randint
from math import sqrt

class InstanceGenerator:
    
    def euclideanDistance(self, point1, point2):
        return sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

    def manhattamDistance(self, point1, point2):
        return abs(point2.x - point1.x) + abs(point2.y - point1.y)

    def generatePoints(self, numberOfPoints):
        points = []
        for _ in range(numberOfPoints):
            X = randint(0, 2000)
            Y = randint(0, 2000)
            newPoint = Point(X, Y)
            points.append(newPoint)
        return points

    def generateGraphEucliedean(self, pointsList):
        TSPGraph = nx.complete_graph(pointsList)
        for n in TSPGraph:
            for nbr in TSPGraph[n]:
                TSPGraph[n][nbr]['weight'] = self.euclideanDistance(n, nbr)
        for p1, p2, eWeight in TSPGraph.edges.data('weight'):
            print(p1, p2, eWeight)
    
    def generateGraphManhattan(self, pointsList):
        TSPGraph = nx.complete_graph(pointsList)
        for n in TSPGraph:
            for nbr in TSPGraph[n]:
                TSPGraph[n][nbr]['weight'] = self.manhattamDistance(n, nbr)
        for p1, p2, eWeight in TSPGraph.edges.data('weight'):
            print(p1, p2, eWeight)

IG = InstanceGenerator()
points = IG.generatePoints(5)
IG.generateGraphEucliedean(points)