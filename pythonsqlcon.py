import mysql.connector as msc
con=msc.connect(host ='localhost', user = 'root', password = '4536', port='3306', database = 'saksham')
cur=con.cursor()
def insert():
    a = int(input('enter the value for s_no\t'))
    b = input('enter the value for Name\t')
    c = input('enter the value for class\t')
    d = input('enter the value for section\t')
    e = int(input('enter the value for phone no\t'))
    f = input('enter the value for Gender\t')
    cur.execute(f'insert into friends values {(a,b,c,d,e,f)}')
    cur.execute('Select * from friends order by s_no')
    for i in cur:
        print(i)
    con.commit()
def deleterow():
    a = int(input('enter the s_no of row to be deleted\t'))
    cur.execute(f'Delete from friends where s_no= {a}')
    cur.execute('select * from friends order by s_no')
    for i in cur:
        print(i)
    con.commit()
if __name__=='__main__':
    while True:
        print ('1.insert')
        print ('2.Delete a row')
        ch = input('enter what you want (1/2)\t')
        if ch == '1' :
            insert()
        elif ch == '2':
            deleterow()
        else :
            break
con.close()