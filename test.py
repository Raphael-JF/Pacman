matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

self.cell_y = len(matrix)
self.cell_x = len(matrix[0])

for sum in range(self.cell_y + self.cell_x - 1):
    start = max(0, sum - self.cell_x + 1)
    end = min(sum, self.cell_y - 1)
    for row in range(start, end + 1):
        col = sum - row
        print(matrix[row][col])