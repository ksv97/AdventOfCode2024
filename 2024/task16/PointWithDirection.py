class PointWithDirection:
    def __init__(self, x, y, direction=(0,1)):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Point: x = {self.x}, y = {self.y}, dir: {self.direction}'

    def __hash__(self):
        return hash(f'x = {self.x}, y = {self.y}')

    def get_cost(self,other):
        if other.direction == self.direction:
            return 1
        elif self.x == -other.x or self.y == -other.y:
            return 1000 * 2 + 1
        else:
            return 1000 + 1