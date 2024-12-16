class lineseg:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.sum_result = 0.

    def sumsq(self):
        self.sum_result = (self.x2 - self.x1)**2 + (self.y2 - self.y1)**2
        return self.sum_result

    def length(self):
        return self.sum_result**0.5

    def __imul__(self, n):
        self.x2 *= n
        self.y2 *= n
        return self

class lineseg3(lineseg):
    def __init__(self, x1=0, y1=0, z1=0, x2=0, y2=0, z2=0):
        super().__init__(x1, y1, x2, y2)
        self.z1 = z1
        self.z2 = z2

    def sumsq(self):
        self.sum_result = super().sumsq() + (self.z2 - self.z1)**2
        return self.sum_result

    def __imul__(self, n):
        super().__imul__(n)
        self.z2  *= n
        return self



line = lineseg(1., 2., 4., 6.)
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())
line *= 2.0
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())

line = lineseg3(1., 2., 3., -1., -2., -3.)
print(line.x1, line.y1, line.z1, line.x2, line.y2, line.z2, line.sumsq(), line.length())
line *= 2.0
print(line.x1, line.y1, line.z1, line.x2, line.y2, line.z2, line.sumsq(), line.length())