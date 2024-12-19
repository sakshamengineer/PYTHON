import pickle as p
f= open('new.dat', 'rb')
n = 0
a = input('enter a word you want to search:\t')
print(f'no of lines starting with {a} is:\t')
while True:
    try:
        c = p.load(f)
        if c[0]==a.lower():
            print(c)
            n+=1
    except:
        break
print(n)