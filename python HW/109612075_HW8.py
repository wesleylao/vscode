#TODO (以下撰寫程式)

s = '1.234'
def leftpad(s, n, c ='0'):
    if n <= len(s):
        return s
    r = (c*(n-len(s)) + s)
    return r[len(r)-n:]
    
print(leftpad(s, 8, 'x'))     # xxx1.234
print(leftpad(s, 8))        # 0001.234
print(leftpad(s, 15, 'ABCD')) # CDABCDABCD1.234
print(leftpad(s, 0))        # 1.234
print(leftpad(n = 7, c = '@', s = s)) # @@1.234

#(以上撰寫程式)
