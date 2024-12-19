a = []
while True:
    print('1.Push')
    print('2.pop')
    print('3.transverse')
    print('to stop')
    ch = input('which operation do you want(1/2/3/4):\t')
    if ch=='1':
        b = input('what do you want to enter in list:\t')
        a.append(b)
        print(f'{a}\n')
    elif ch == '2':
        if a == []:
            print('stack is underflow \n')
        else :
            print('your Poped item is',a.pop())
            print(f'{a}\n')
    elif ch=='3':
        a.reverse()
        print(a)
        print()
    elif ch == '4':
        break
    else:
        print('invalid input')
        continue