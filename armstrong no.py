def check():
    a = int(input('enter a no.\t'))
    b = f'{a}'
    c = len(b)
    r = 0
    for i in b:
        r+=int(i)**c

    if r==a:
        print('yes it is armstrong no.\n')
    else:
        print('no it is not armstrong no.\n')
def mate():
    a1 = int(input('from where:\t'))
    a = int(input('to where:\t'))
    b = []
    for i in range(a1,a+1):
        c = f'{i}'
        d = len(c)
        e = 0
        for j in c:
            e+=int(j)**d
        if e==i:
            b.append(e)
    print(*b,sep=", ")

while True:
    print('1.to check no. is armstrong or not')
    print("2.to get armstrong no's between two range")
    print('3.to stop')
    cho = input('what do you want(1/2/3):\t')
    if cho == '1':
        check()
    elif cho == '2':
        mate()
    elif cho == '3':
        break
    else:
        print('invalid input')
        continue