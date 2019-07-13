from numpy.linalg import norm
from numpy import array, append, arange, fabs, empty


def radius_search(query, radius, node, neighbors=None):
    if neighbors is None:
        neighbors = empty((0, len(query)), float)
    if node is None:
        return neighbors

    axis = node.axis
    if query[axis] < node.location[axis]:
        here = node.leftChild
        there = node.rightChild
    else:
        here = node.rightChild
        there = node.leftChild

    neighbors = radius_search(query, radius, here, neighbors)

    if fabs(query[axis] - node.location[axis]) <= radius:
        if norm(query - node.location) <= radius:
            neighbors = append(neighbors, [node.location], axis=0)
        neighbors = radius_search(query, radius, there, neighbors)

    return neighbors
