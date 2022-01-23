class Matrix():
    def __init__(self, rows = 2, columns = 2, grid = [[1, 0], [0, 1]]):
        for row in grid:
            if len(row) != columns:
                raise DimensionalError("Invalid columns")
        if len(grid) == rows:
            self.grid = grid
            self.order = (rows, columns)
            if rows == columns:
                self.determinant = determinant(grid)
        else:
            raise DimensionalError("Number of rows do not match")
    def transpose(self):
        buffer = self.grid
        new_grid =[]
        for i in range(self.order[1]):
          new_grid.append([])
          for j in range(self.order[0]):
            new_grid[i].append(buffer[j][i])
        self.grid = new_grid
        self.order = (self.order[1],self.order[0])
    def inverse(self):
        d = self.determinant
        if d != 0:
            aa = self.grid[0][0] / d
            ab = self.grid[0][1] / d
            ba = self.grid[1][0] / d
            bb = self.grid[1][1] / d
            self.grid = [[bb, -ab], [-ba, aa]]
        else:
            print('non-invertible.')
    def multiply(self1,self2):
        aa = self1.grid[0][0] * self2.grid[0][0] + self1.grid[0][1] * self2.grid[1][0]
        ab = self1.grid[0][0] * self2.grid[0][1] + self1.grid[0][1] * self2.grid[1][1]
        ba = self1.grid[1][0] * self2.grid[0][0] + self1.grid[1][1] * self2.grid[1][0]
        bb = self1.grid[1][0] * self2.grid[0][1] + self1.grid[1][1] * self2.grid[1][1]
        self1.product= [[aa, ab], [ba, bb]]        

class NonInvertibleMatrix(Exception):
    pass
class DimensionalError(Exception):
    pass        
