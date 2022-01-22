import math
from copy import deepcopy 

def sub_matrix(matrix, rows, column)
    new_matrix = deepcopy(matrix)
    new_matrix.remove(matrix[row, 1])
    for i in range(len(new_matirx)):
        new_matrix[i].remove(new_matrix[i][column])
    return new_matrix    

def determinant(matrix):
    rows = len(matrix)
    for rows in matrix:
        if len(rows) != rows:
            print("not a square matrix.")
            return none
        if len(matrix) == 2:
            simple_determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return simple_determinant
        else:
            det = 0
            columns = rows
            for j in range(columns):
                cofactor = (-1) ** j * matrix[0][j]\
                           * determinant(sub_matrix(matrix, 0, j))
                det += cofactor
            returm det    

class Vector():
    def __init__(self, a, b):
        self.norm = (a**2 + b**2) ** 0.5
        self.arg = math.atan(b / a)
        self.grid = [a, b]
        self.slope = b / a
    def visualise(self):
        plt.plot(self.grid[0], self.grid[1])
        plt.show()


class Matrix():
    def __init__(self, rows = 2, columns = 2, grid = [[1, 0], [0, 1]]):
        for row in grid:
            if len(row) != columns:
                raise DimensionalError("Invalid columns")
        if len(grid) == rows:
            self.grid = grid
            if rows == columns:
                self.determinant = determinant(grid, rows)
        else:
            raise DimensionalError("Number of rows do not match")
    def transpose(self):
        aa = self.grid[0][0]
        ab = self.grid[0][1]
        ba = self.grid[1][0]
        bb = self.grid[1][1]
        self.grid = [[aa, ba], [ab, bb]]
    def invert(self):
        d = self.determinant
        if d != 0:
            aa = self.grid[0][0] / d
            ab = self.grid[0][1] / d
            ba = self.grid[1][0] / d
            bb = self.grid[1][1] / d
            self.grid = [[bb, -ab], [-ba, aa]]
        else:
            raise NonInvertibleMatrix
    def multiply(self, B):
        if type(B) == Matrix:
            Aaa = self.grid[0][0]
            Aab = self.grid[0][1]
            Aba = self.grid[1][0]
            Abb = self.grid[1][1]
            Baa = B.grid[0][0]
            Bab = B.grid[0][1]
            Bba = B.grid[1][0]
            Bbb = B.grid[1][1]
            Paa = Aaa*Baa + Aab*Bba
            Pab = Aaa*Bab + Aab*Bbb
            Pba = Aba*Baa + Abb*Bba
            Pbb = Aba*Bab + Abb*Bbb
            return Matrix(Paa, Pab, Pba, Pbb)
        elif type(B) == Vector:
            Aaa = self.grid[0][0]
            Aab = self.grid[0][1]
            Aba = self.grid[1][0]
            Abb = self.grid[1][1]
            Ba = B.grid[0]
            Bb = B.grid[1]
            Pa, Pb = Aaa * Ba + Aab * Bb, Aba * Ba + Abb * Bb
            return Vector(Pa, Pb) 

class NonInvertibleMatrix(Exception):
    pass
class DimensionalError(Exception):
    pass
