from classes.node import Node
from matplotlib import pyplot as plt
from matplotlib import patches


class QuadTree:
    def __init__(self, threshold):
        self.threshold = threshold
        self.root = Node(0, 0, 10, 10, None)
        
    def add_point(self, x, y):
        self.root.add_point(x, y)

    def get_points(self):
        self.root.get_points()

    def subdivide(self):
        recursive_subdivide(self.root, self.threshold)

    def graph(self):
        fig = plt.figure(figsize=(12, 8))
        plt.title("Quadtree")
        ax = fig.add_subplot(111)
        c = find_children(self.root)
        print(f"Number of segments: {len(c)}")
        areas = set()
        for el in c:
            areas.add(el.width * el.height)
        print(f"Minimum segment area: {min(areas)}")
        for n in c:
            ax.add_patch(patches.Rectangle((n.x, n.y), n.width, n.height, fill=False))
        x = [point.x for point in self.root.points]
        y = [point.y for point in self.root.points]
        c = [point.data['color'] for point in self.root.points]
        red_patch = patches.Patch(color='red', label='Gas Station')
        blue_patch = patches.Patch(color='blue', label='Police')
        yellow_patch = patches.Patch(color='yellow', label='Hospital')
        plt.legend(handles=[red_patch, blue_patch, yellow_patch])
        plt.scatter(x, y, c=c)
        plt.show()
        return


def recursive_subdivide(node, k):
    if len(node.points) <= k:
        return

    w_ = float(node.width / 2)
    h_ = float(node.height / 2)

    p = contains(node.x, node.y, w_, h_, node.points)
    x1 = Node(node.x, node.y, w_, h_, p)
    recursive_subdivide(x1, k)

    p = contains(node.x, node.y + h_, w_, h_, node.points)
    x2 = Node(node.x, node.y + h_, w_, h_, p)
    recursive_subdivide(x2, k)

    p = contains(node.x + w_, node.y, w_, h_, node.points)
    x3 = Node(node.x + w_, node.y, w_, h_, p)
    recursive_subdivide(x3, k)

    p = contains(node.x + w_, node.y + h_, w_, h_, node.points)
    x4 = Node(node.x + w_, node.y + h_, w_, h_, p)
    recursive_subdivide(x4, k)

    node.children = [x1, x2, x3, x4]


def contains(x, y, w, h, points):
    pts = []
    for point in points:
        if x <= point.x <= x + w and y <= point.y <= y + h:
            pts.append(point)
    return pts


def find_children(node):
    if not node.children:
        return [node]
    else:
        children = []
        for child in node.children:
            children += (find_children(child))
    return children
