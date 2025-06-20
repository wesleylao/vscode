class Triangle_Calculation:
    def __init__(self, *arr: list[int]):
        self.arr = arr
        self.perimeter_result = self.__Perimeter()
        self.area_result = self.__Area()
    def __Perimeter(self):
        result = []
        for arr in self.arr:
            l = sum(arr)
            result.append(l)
        return result
    def __Area(self):
        result = []
        for arr in self.arr:
            tmp = sum(arr)/2
            a = (tmp*(tmp-arr[0])*(tmp-arr[1])*(tmp-arr[2]))**0.5
            result.append(a)
        return result

A = [5, 4, 3]
B = [4, 5, 6]
C = [7, 8, 9]
c = Triangle_Calculation(A, B, C)
print("perimeter = ", c.perimeter_result, "\n", "area =", c.area_result)