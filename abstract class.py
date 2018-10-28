from abc import ABC,abstractmethod

class employee(ABC):

    @abstractmethod

    def calculate_salary(self, sal):

        sal += 10
        #pass
emp1 = developer()
emp1.sal = (1500)
print(emp2.calculate_salary(1500))
class developer(employee):

     def calculate_salary(self,sal):

         final_sal = sal * 1.10

         return  final_sal

emp1 = developer()
print(emp1.calculate_salary(1500))

