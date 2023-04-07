import sys

import numpy as np
import pygame
from contracts import *
from settings import *
import random

class Generator:
    def __init__(self):
        self.cols = 0
        self.rows = 0
        self.grid = np.NAN
        self.empty_position_count = 0

    def generate_maze(self, rows, cols):
        zero_counter = 0
        v = 0
        grid = np.full_like(np.zeros((rows, cols)), fill_value=BLOCKED, dtype=int)
        for i in range(rows):
            for j in range(cols):
                if i % 2 == 1 and j % 2 == 1:
                    grid[i, j] = PASSAGE
                    zero_counter += 1
        self.cols = cols
        self.rows = rows
        self.grid = grid
        self.empty_position_count = zero_counter
        current_cell = (1, 1)
        stack = []
        visited = [current_cell]
        while v < zero_counter - 1:
            all_neighbors = self.get_neighbors_of_cell(current_cell, PASSAGE)
            neighbors = []
            for n in all_neighbors:
                if n not in visited:
                    neighbors.append(n)
            next_cell = []
            if neighbors:
                next_cell = random.choice(neighbors)
            if next_cell:
                visited.append(next_cell)
                stack.append(current_cell)
                self.connect_cell(current_cell, next_cell)
                current_cell = next_cell
                self.grid[current_cell] = PASSAGE
                v += 1
            elif stack:
                current_cell = stack.pop()
