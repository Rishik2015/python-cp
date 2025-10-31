import random
number = random.randint(1,10)

def intro():
    print("May i ask your name ??????")
    global name
    name = input()
    print(name + ",we are going to play a game. I am thinking of anumber bestween 1 to 10")
    if(number%2==0):
        x= 'even'
    else:
        x= 'odd'    
    print ("\nthis is an {} number".format(x)) 
    print("Go ahead guess")  
def pick():
    guessesTaken = 0
    while guessesTaken < 100:
        enter=input("guess:")
        try:
            guess =  int(enter)
            if guess<=10 and guess<=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<100:
                    if guess>number:
                        print('the guess of the number you have entered is too high')
                    if guess<number:
                        print('the guess of the number you have entered is too low')    
                    if guess  != number:
                        print ('Try Again')  
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print ("silly goose!that number is not in the range")       
                print('enter a number bestween 1 to 10')    
        except:
            print("i dont think that"+enter+"is a number")   
            
    if guess ==  number:
        print('good job {} you guessed mynumber in{} guesses'.format(name,guessesTaken))   
    if guess != number:
        print("nope."+ str(number))  
  
intro()
pick()