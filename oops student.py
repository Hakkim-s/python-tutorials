class student():
     def __init__(self,sex,dob,year_of_passing,rank):
         self.sex = sex
         self.dob = dob
         self.year_of_passing = year_of_passing
         self.rank = rank
     def final_rank(self):
         self.rank = (self.rank * 3)


#class objects
hakkim = student('male','20-05-1996',2017,1)
print(hakkim.__dict__)
hakkim.char = 'jovial'
aditi = student("female",'19-feb-1996',2017,1)
print(aditi.__dict__)
print(hakkim.char)
print(hakkim.rank)
print(aditi.year_of_passing)
hakkim.final_rank()
print(hakkim.rank)