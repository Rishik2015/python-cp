# #class 1

# class India():
#     def capital(self):
#         print("NEW DELHI is the capital of INDIA")

#     def language(self)    :
#         print("HIINDI BHARAT KI SABSE JYADA BOLNE JANE VALI BHASHA HAI|")

#     def type(self)   : 
#         print("INDIA is a developing country")


# class USA():
#     def capital(self):
#         print("WASHINGTON D.C. is the capital of USA")

#     def language(self)    :
#         print("ENGISH is the primaary language of USA")

#     def type(self)   : 
#         print("USA is a developing country")

# obj_ind = India()       
# obj_usa = USA() 

# for country in (obj_ind , obj_usa):
#     country.capital()
#     country.language()
#     country.type()

from abc import ABC, abstractmethod

class Absclass(ABC):
    def print (self,x):
        print("PASSED VALUE",x)

    @abstractmethod
    def task(self)    :




        print("WE ARE IN ABSCLASS TASK")
class test_class(Absclass)  :
    def  task(self) :
        print("WE ARE IN TEST CLASS TASK")     

test_obj       = test_class()
test_obj.task()
test_obj.print(100)