import math

class Vector():
    def __init__(self, a, b):
        self.norm = (a**2 + b**2) ** 0.5
        self.arg = math.atan(b / a)
        self.grid = [a, b]
        self.slope = b / a

class Matrix():
    def __init__(self, aa, ab, ba, bb):
        self.grid = [[aa, ab], [ba, bb]]
        self.determinant = aa * bb - ab * ba
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
