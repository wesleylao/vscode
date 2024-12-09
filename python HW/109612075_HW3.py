# rows = 5 
# columns = 5
# L = []
# L = ""

################################
#TODO
x = int(input())
y = int(input())
r = "o"
while x != 0:
    s = ""
    tmp = y
    while tmp != 0:
        s += r
        r = "x" if r == "o" else "o"  
        tmp = tmp - 1
    r = "x" if s[0] == "o" else "o"
    print(s)    
    x = x - 1
#TODO
################################

# print(L)