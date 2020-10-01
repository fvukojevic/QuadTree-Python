from classes.point import Point


class Node:
    def __init__(self, x, y, w, h, points):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.points = points
        self.children = []

    def set_points(self, points):
        self.points = points

    def add_point(self, x, y):
        self.points.append(Point(x, y))

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_points(self):
        return self.points
