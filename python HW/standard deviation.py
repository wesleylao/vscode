class Standard_Deviation:
    def __init__(self, *arr: list[int]):
        self.arr = arr
        self.identity_result = self.__Identity()
        self.calculation_result = self.__Calculation()
    def __Calculation(self):
        result = []
        for arr in self.arr:
            a = sorted(arr)
            a_len = len(a)
            mean_arr = sum(a)/a_len
            i = 0
            tmp = 0
            tmp2 = 0
            while i < a_len:
                tmp = (a[i]-mean_arr)**2
                tmp2 += tmp
                i += 1
            std = (tmp2/(a_len-1))**0.5
            result.append(std)
        return result
    def __Identity(self): 
        result = []
        for arr in self.arr:  
            b = sorted(arr)
            b_len = len(b)
            max_arr = b[-1]
            min_arr = b[0]
            if b_len % 2 == 1:
                median_arr = b[b_len//2]
            else:
                median_arr = (b[b_len//2]+b[b_len//2-1])/2
            result.append([max_arr, min_arr,median_arr])
        return result


A = [10, 5, 1, 6, 9, 2, 6, 9, 10, 8]
B = [13, 9, 1, 8, 10, 7, 3, 4, 18, 2]
C = [86, 10, 26, 66, 97, 35, 69, 31, 89, 67]
a = Standard_Deviation(A,B,C)
print('max, min, median = ', a.identity_result, '\n', 'standard deviation = ', a.calculation_result)
        