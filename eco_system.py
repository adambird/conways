from random import *

class EcoSystem(object):
    def __init__(self, size):
        self.size = size
        self.rows = self.generate_blank_rows(size)

    def generate_blank_rows(self, size):
        rows = [0] * size
        for i in range(size):
            rows[i] = [0] * size
        return rows

    def cell_state(self, x, y):
        return self.rows[y][x]

    def set_alive(self, x, y):
        self.rows[y][x] = 1

    def set_dead(self, x, y):
        self.rows[y][x] = 0

    def seed(self):
        for y in range(self.size):
            for x in range(self.size):
                if random() > 0.5:
                    self.set_alive(x,y)
                else:
                    self.set_dead(x,y)

    def number_of_neighbours(self, x, y):
        neighbour_count = 0

        for nx in range(x-1, x+2):
            if -1 < nx < self.size:
                for ny in range(y-1, y+2):
                    if -1 < ny < self.size:
                        if not (nx == x and ny == y):
                            neighbour_count += self.cell_state(nx, ny)

        return neighbour_count

    def next_generation_cell_state(self,x, y):
        neighbour_count = self.number_of_neighbours(x, y)
        current_state = self.cell_state(x, y)

        if current_state == 1:
            if neighbour_count < 2 or neighbour_count > 3:
                return 0
            else:
                return 1
        else:
            if neighbour_count == 3:
                return 1
            else:
                return 0


    def advance_generation(self):
        new_rows = self.generate_blank_rows(self.size)
        for y in range(self.size):
            for x in range(self.size):
                new_rows[y][x] = self.next_generation_cell_state(x, y)

        self.rows = new_rows







