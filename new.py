a = int(input("enter a no.\t"))
b = 0
for i in range(1,a):
    if a>1:
        if a%i == 0:
            b+=1
        else:
            pass
    else:
        b-=1
print(b)
if b>1:
    print('it is not prime no.')
elif b==1:
    print("it is prime no.")
else:
    print('it is neither prime nor composite ')