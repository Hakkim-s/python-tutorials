#intro
num1 = 1
num2 = 2
print("num1 + num2:",num1 + num2)
print(num1)
print(num2)
num3 = num1
num1 = num2
num2 = num3
print(num1)
print(num2)
print(7)
#if_else
if num1 < num2:
    print("<num1 is less than num2")
elif num1 == num2:
    print("num1 equals to num2")
elif num1 > num2 + 20:
    print('num1 is greater than num2 by adding 20')
else:
    print("num2 is greater")
print("i did it")
num1 = 2
num2 = 1
if num1 < num2:
    print("num1 is less than num2")
else:
    if num1 == num2:
        print("both are equals")
    else:
        print("num1 is greater than num2")

print ("Roosters", 100 - 25 * 4 % 4)

name = "hakk"
height_m = 1.5
weight_kg = 90

bmi = weight_kg / (height_m ** 2)
print("bmi:",bmi)
if bmi < 25:
    print(name)
    print("he is not over weight")
else:
    print(name)
    print(" he is overweight")

name = "hakk"
my_age = 21
print(round(1.55))
print ("myself %r" % name)
print('My age is %u' % my_age)

my_age = "my age is %d and his age is  %d" %(21,32)
print(my_age)
name = "my name is %s and am from %s..."  % ("hakk","india")
print(name)
print(name + my_age)
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)
#functions
def function3():
    print('hehehe')
    print("hehehe 2")
print('outside the function1')

function3()
function3()
def function2(x):
    return 2*x
a = function2(8)
print('a =',a)
b = function2(5)
print('b = ',b)

def function1(x,y):
    return  x + y
c = function1(27,35)
print("c =",c)

def function4(x):
    print(x)
    print("still here")
    return 3 * x
f = function4(4)
print('f =',f)

def function5(abcd):
    print(abcd)
    print('1234')
function5(5678)'''

'''name1 = "hakk"
weight_k1 = 90
height_m1 = 1.79
name2 = "abul"
weight_k2 = 70
height_m2 = 1.79
name3 = "dinesh"
weight_k3 = 50
height_m3 = 1.5

def bmi_calci(name,weight_k,height_m):
    bmi = weight_k / (height_m ** 2)
    print('BMI =',bmi)
    if bmi < 25:
        return name + " should not reduce the weight"
    else:
        return name + ' must reduce the weight'
result1 = bmi_calci(name1,weight_k1,height_m1)
result2 = bmi_calci(name2,weight_k2,height_m2)
result3 = bmi_calci(name3,weight_k3,height_m3)
print(result1)
print(result2)
print(result3)


def convert(miles):
    return 1.6 * miles
km = convert(8)
print("km =",km)

def function2(x):
    return 2*x
a = function2(8)
print('a =',a)
#lists
a = [1,2,3]
print(a)
a.append(4)
print(a)
a.append('ready')
print(a)
a.append([5,6])
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)

print (a[0])
print(a[2])
a[2] = 100
print(a[2])
print(a)
a.append('ready')
print(a)
a.append('hakkim')
print(a)

b = ["king","queen","jack"]
print(b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
b[0],b[2] = b[2],b[0]
print(b)
b.append ('mouse')
print(b)
b[0],b[3] = b[3],b[0]
print(b)
#for_loop
for ele in b:
    print(ele)
    print(ele)
c = [27,56,78]
total = 1
for cyc in c:
    total = total + cyc
print(total)

d = list(range(0,100))
#print(d)
total = d + list(range(101,2000))
#print(total)
#for ert in d:
    #print(ert)
total2 = 0
for qwe in range(0,100):
    total2 += qwe
print(total2)

print(list(range(1,30)))
total3 = 0
for tyu in range(1,30):
    if tyu % 3 == 0:
        total3 += tyu
print(total3)
print('string '*2)
#whileloop
total4 = 0
j = 1
while j < 5:
    total4 +=j
    j += 1
print(total4)

this_list = [5,8,5,6,1,1,-8,-8]
total5 = 0
i = 0
while i < len(this_list) and this_list[i] > 0:
    total5 += this_list[i]
    i += 1
print(total5)

#mightbeforloop
#this_list2 = [5,8,5,6,1,1,-8,-8]
total6 = 0
for ele in this_list:
    if ele <= 0:
        break
    total6 += ele
print(total6)
#while with break
total7 = 0
i = 1
while True:
    total7 += this_list[i]
    i += 1
    if this_list[i] <= 0:
        break
print(total7)
this_list2 = [5,8,5,6,1,1,-8,-5,-3,-1]
total7 = 0
i = 7
while  this_list2[i] > 0:
    total7 += this_list2[i]
    i += 1
print(total7)

#weightcalci
name = "hakk"
height_m = 1.8
#weight_kg = 90
bmi = 27.777777777777775
weight_kg = bmi * (height_m ** 2)
bmi = weight_kg * (height_m ** 2)
#print(bmi)
print("weight:",weight_kg)
if weight_kg < 90.0:
    print(name)
    print("he is not over weight")
else:
    print(name)
    print(" he is overweight")
#again for loop

things =['raja','rani','madhri']
print(things)
for things2 in things:
    print(things2)

for things2 in range(0,3):
    print(things[things2])

for things2 in range(len(things)):
    print(things[things2])

for things2 in range(len(things)):
    for j in range(things2 + 1):
      #things = 0 -> j = 0
      #things = 1 -> j = 0,1
      #things = 3 -> j = 0,1,2
        print(things[things2]) '''
print(list(range(0,100)))
total7 = 0
for i in range(0,100):
    if i % 3 == 0 or i % 5 == 0:
        total7 += i
print('totally =',total7)


given_list = [9,8,7,6,5,-5,-6,-7,-8,-9]
total8 = 0
j = len(given_list)-1
while given_list[j]<0:
    total8 += given_list[j]
    j -= 1
print(total8)

total9 = 0
i = 1
while True:
    total9 += given_list[i]
    i += 1
    if given_list[i] < 0:
        break
print(total9)
#how to use dictionaries in python


d = {"hakkim": 21,"abul": 19}
d["hakkim"] =  21
d["abul"] = 19
print(d["abul"])
print(d["hakkim"])
print("after swapping:")
d["temp"] = d["abul"]
d["abul"] = d["hakkim"]
d["hakkim"] = d["temp"]
d[100] = 10
print(d["abul"])
print(d["hakkim"])
print("key with values:")
for key, value in d.items():
    print("-->key")
    print(key)
    print("-->value")
    print(value)
    print("")