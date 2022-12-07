import networkx as nx

from math import sqrt

def euclideanDistance(point1, point2):
    return sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

def manhattamDistance(point1, point2):
    return abs(point2.x - point1.x) + abs(point2.y - point1.y)



