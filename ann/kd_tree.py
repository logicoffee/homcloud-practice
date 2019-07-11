from numpy import array, random, concatenate
from math import ceil
from quick_select import quick_select


class Node:
    def __repr__(self):
        return str(self.location) + ': [\n\t' + repr(self.leftChild) + '\n\t' + repr(self.rightChild) + '\n]'


def kdtree(pointList, depth=0):
    if len(pointList) == 0:
        return

    k = len(pointList[0])
    axis = depth % k

    median = quick_select(pointList[:, axis], len(pointList) // 2 + 1)
    middle = pointList[pointList[:, axis] == median]
    left = pointList[pointList[:, axis] < median]
    right = concatenate([pointList[pointList[:, axis] > median], middle[1:]])

    node = Node()
    node.location = middle[0]
    node.leftChild = kdtree(left, depth+1)
    node.rightChild = kdtree(right, depth+1)
    return node
