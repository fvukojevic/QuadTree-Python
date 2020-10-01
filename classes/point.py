class Point:
    def __init__(self, x, y, data):
        self.data = data
        self.x = x
        self.y = y

    def __str__(self):
        return 'P({:.2f}, {:.2f})'.format(self.x, self.y)