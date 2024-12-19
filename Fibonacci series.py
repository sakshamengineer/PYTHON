def cho1():
    z = input('want to continue?(y/n):\t')
    if z == 'y':
        pass
    else:
        quit()
def Fibonacci(n):
    x = 0
    y = 1
    z = y
    count= 1
    print(x)
    print(y)
    while count<= n-2:
        print(z,end="\n")
        count+=1
        x=y
        y=z
        z= x+y
while True:
    n = int(input('enter the range of series:\t'))
    Fibonacci(n)
    cho1()
