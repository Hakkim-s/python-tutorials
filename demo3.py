#string

string1 = 'community'
string2 = 'jungle'
string3 = "e,a,g,l,e"

print(string1  + string2)

print(string2 * 8)
#slicing
print(string1[:-2])
print(string1[5:-2])
#find
print (string1.find('unity'))
#replace
print(string1.replace('comm',"the world of "))
#split
print(string3.split(','))
#count
print(string1.count('m',0,6))
print(string3.count('e',0,4))
#upper
print(string2.upper())
#max
print(max(string1))
#min
print(min(string1))
#is.............
print(string2.isspace())
print(string2.isalpha())
print(string3.isidentifier())

#tuples

my_tup = ('hakkim','abul',"jarina","shaik")

#concatenation

print(my_tup+("vj",'make change'))

#repitition
print(my_tup * 5)

#slicing
print(my_tup[0:2])
print(my_tup[-1])

#indexing
print(my_tup[2])


#lists

my_list = [1,2.5,"vj"]
print(my_list)
#append
my_list.append('h')
print(my_list)
#extend
my_list.extend([2.5,1])
print(my_list)
#insert
my_list.insert(1,2)
my_list.insert(-1,2)
print(my_list)
#pop
my_list.pop(2)
print(my_list)


#dictionary

my_dict = {1:'billa',2:"bong",3:'school'}
print(my_dict)
#keys
print(my_dict.keys())
#values
print(my_dict.values())
#item
print(my_dict.items())
#get
print(my_dict.get(2))
#update
my_dict.update({4:'chennai'})
print(my_dict)
my_dict.pop(4)
print(my_dict)

#sets

my_set = {2,4,8,5,1,45,69,1,100,45,1,1,0,4,5,"kdjcd","hjfkjfd"}
my_set1 = {"djnd","kdjcd","hjfkjfd",45,0,5,4,69,8,1,2,}
print(my_set)
print(my_set1)
#union
print("union:",my_set | my_set1)
#intersection
print("intersection:",my_set & my_set1)
#difference
print("difference:",my_set - my_set1)



