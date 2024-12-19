import csv 
f = open('new.csv','w',newline='\n')
a = csv.writer(f)
l = []
while True:
    b = int(input('enter s_no:\t'))
    c = input('enter name:\t')
    d = int(input('enter roll_no:\t'))
    e = [b,c,d]
    l.append(e)
    cho = input('do you want to add more data?(y/n):\t')
    if cho.lower()=='y':
        continue
    else:
        break
for i in l:
    a.writerow(i)
f.close()
