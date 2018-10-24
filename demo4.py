import http
#if_elif_else
'''
cgp = 4
if(cgp>8):
    print("FIRST CLASS")
elif(cgp>6) and (cgp<=8):
    print("SECOND CLASS")
elif(cgp>4) and (cgp<=6):
    print("THIRD CLASS")
elif(cgp>=3) and (cgp<=4):
    print("FOURTH CLASS")
else:
    print("FAIL")

#while

num = float(input('Enter the values of N ='))
if(num<=0):
    print('Enter the valid value')
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
print(sum)

ec =5
d = str(ec)+"jingle bell jingle bell" + "single bell single bell"
print(d)

#break

count = 0
while True:
    print(count)
    count += 1
    if(count > 20):
        break

#continue

for w in range(20):
    if (w%2)== 0:
        continue
    print(w)


#even  or odd
num = int(input("Enter the number:"))
mod = num%2
if mod == 0:
    print('even')
else:
    print('odd')

'''

def fuc():
    return 0
print(fuc())

#fibonacci

def fibo(n):
    a =0
    b =1
    for x in range(n):
        a = b
        b = a+b
        print(a,'\n')
    return b
num = int(input("<H3>Enter the value of n:<H3>"))
print(fibo(num))

#filehandling

fb = open("D:\\wallpaper\\py.txt",'r+')
fb.write("hakkim your are always smart \n")
fb.write("Aditi is good girl da,she is very perfect for you")
fb.seek(35)
print(fb.read())
fb.close()




