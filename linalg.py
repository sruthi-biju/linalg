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
