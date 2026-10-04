import math
import random
import time


class Bit:
    def __init__(self, x, y, bias = 0):
        self.x = x
        self.y = y
        self.value = random.choice([-1, 1])
        self.bias = bias

    def calculate_value(self, grid, j = 1, t = 1):
        def sigmoid(x):
            return 1 / (1 + math.exp(-x))

        rows = len(grid)
        cols = len(grid[0])

        neighbors = [
            grid[(self.x - 1) % rows][self.y].value,
            grid[(self.x + 1) % rows][self.y].value,
            grid[self.x][(self.y - 1) % cols].value,
            grid[self.x][(self.y + 1) % cols].value
        ]
        s = sum(neighbors) * j + self.bias

        p = sigmoid(2 * s / t)

        rand = random.uniform(0, 1)
        if rand <= p:
            self.value = 1
        else:
            self.value = -1

if __name__ == '__main__':
    size = 40
    step = 0
    j = 1
    t = 2.27

    # todo jakos zaprogramowac/zaprojektowac ten algorytm
    # model Isinga czy cos takiego
    # czy da sie 3d/4d/nd
    grid = [[Bit(x, y) for y in range(size)] for x in range(size)]

    while True:
        step += 1
        for _ in range(size * size):
            rx = random.randint(0, size - 1)
            ry = random.randint(0, size - 1)
            grid[rx][ry].calculate_value(grid, j, t)

        print("\033[H", end="")
        print(f"\n-------------- Step {step} ---------------")
        for row in grid:
            print("".join(["█" if bit.value == 1 else " " for bit in row]))

        time.sleep(0.05)