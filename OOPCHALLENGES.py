# class A :
#     def __init__(self ,a):
#         self.a = a
#     def __lt__(self , other)    :
#         if(self.a<other.a):
#             return "ob1 is less than ob2"
#         else:
#             return "ob1 is less ob2"
#     def __eq__(self,other):
#         if(self.a == other.a)  :
#             return "both obama are  equaaal"  
#         else:
#             return "Both aaaaaaaaaaaaaare not equal"
        
# ob1 = A(2)        
# ob2 = A(3)
# print("PASsed values: ",ob1.a, ob2.a)
# print(ob1 < ob2)
# ob3 = A(4)
# ob4 = A(4)
# print("PASsed values: ",ob3.a, ob4.a)
# print(ob3 == ob4)
import  random
class Fruit:
    def __init__(self):
        self.fruits
        {"apple" : "red",
                    "orange" :  "orange",
                    'kiwi' : "green"}
    def quiz (self)   :
        while (True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            user_answer = input()
            if(user_answer.lower() == color):
                print("CORECT")
            print("wrong")    
            option = int(input("enter 0 if you want to continue or enter 1"))
            if(option):
                break
print("WELCOME TO FRUIT QUIZ")
fq = Fruit()
fq.quiz

