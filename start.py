from classes.quadTree import QuadTree
from classes.point import Point
from numpy import random


def random_point_data(items):
    return random.choice(items)


if __name__ == '__main__':
    pointItems = [
        {
            'name': 'gas_station',
            'color': 'red'
        },
        {
            'name': 'hospital',
            'color': 'yellow'
        },
        {
            'name': 'police',
            'color': 'blue'
        }
    ]
    points = [Point(random.uniform(0, 10), random.uniform(0, 10), random_point_data(pointItems)) for x in range(1000)]
    quadTree = QuadTree(3)
    quadTree.root.set_points(points)
    quadTree.subdivide()
    quadTree.graph()
