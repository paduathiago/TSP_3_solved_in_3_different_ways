import networkx as nx

from random import randint
from math import sqrt
from point import Point

def euclideanDistance(point1, point2):
    return sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

def manhattamDistance(point1, point2):
    return abs(point2.x - point1.x) + abs(point2.y - point1.y)

def generatePoints(numberOfPoints):
    points = []
    for _ in range(numberOfPoints):
        X = randint(0, 2000)
        Y = randint(0, 2000)
        newPoint = Point(X, Y)
        points.append(newPoint)

def generateGraph(pointsList):
    nx.complete_graph(pointsList)

generatePoints(5)