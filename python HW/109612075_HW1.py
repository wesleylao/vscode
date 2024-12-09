price, payment = map(int, input("input price and payment in one line, use ',' to separate two paremeters: ").split(","))
if payment >= price:
    tmp = payment - price
    for nt in [50, 10, 5, 1]:
        print(f"{nt}*{int(tmp/nt)}")
        tmp = tmp%nt
else:
    print('payment is not enough')