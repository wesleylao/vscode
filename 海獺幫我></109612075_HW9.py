class lineseg:
    #TODO (以下撰寫程式)


    #(以上撰寫程式)


class lineseg3(lineseg):
    #TODO (以下撰寫程式)


    #(以上撰寫程式)



line = lineseg(1., 2., 4., 6.)
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())
line *= 2.0
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())

line = lineseg3(1., 2., 3., -1., -2., -3.)
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())
line *= 2.0
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())