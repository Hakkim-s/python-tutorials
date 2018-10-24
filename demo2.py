'''you_hve = input('Enter the amount:')
i_hve = input('Enter the amount:')
p = 'you having %s and i having %r' %(you_hve,i_hve)
print(p)'''

from sys import argv

script, first, second, third = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
all()
