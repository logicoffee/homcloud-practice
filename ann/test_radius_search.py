from numpy import array, sin, cos, random, apply_along_axis, append
from kd_tree import kd_tree
from radius_search import radius_search


def test_radius_search():
    # 10 neighbors
    neighbors_unit_circle = array([[cos(x), sin(x)] for x in random.rand(10)])
    expected_neighbors = apply_along_axis(
        lambda x: random.rand() * x, 1, neighbors_unit_circle)

    randoms_unit_circle = array([[cos(x), sin(x)] for x in random.rand(1000)])
    other_points = apply_along_axis(
        lambda x: (random.rand() + 1) * x, 1, randoms_unit_circle)

    point_cloud = append(expected_neighbors, other_points, axis=0)
    random.shuffle(point_cloud)

    node = kd_tree(point_cloud)
    neighbors = radius_search([0., 0.], 1., node)
    assert len(neighbors) == 10
    for neighbor in neighbors:
        assert neighbor in expected_neighbors
