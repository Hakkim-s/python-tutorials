'''def print_func(par):
 print("Hello: ",par)
 return

import _osx_support

_osx_support.print_func('zara')


from fib import fibonacci


import math

content = dir(math)

print(content)


reload(hello)
#namespacing and scoping
money = 2000
def Addmoney():
     global money
money = money + 1
print(money)
#Addmoney()
print(money)

def pots():
    print("Im Pots phone") '''

x = "this is that "
xx ="152588465.2"
y = 10
#int(x[100,base])

print(str(x))
print(str(x))
print(float(xx))
print((xx))

print(tuple(str("100")))

def some_function():
    for i in range(4):
        yield i

for i in some_function():
    print (i)
'''
from sys import argv


script,first,2nd,3rd = argv

print("one:",script)
print("two:",first)
print("three:",2nd)
print("four:",3rd)
'''


from sys import argv

script, user_name = argv
prompt = '> '
print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = raw_input(prompt)

print ("Where do you live %s?" % user_name)
lives = raw_input(prompt)
print ("What kind of computer do you have?")
computer = raw_input(prompt)

print (""")
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. % (likes, lives, computer)