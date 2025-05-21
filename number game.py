import random 
def guess_number():
    guess_number=random.randint(1,100)#range of the number to guess
    attempts=0
    while True:
        try:
            guess=int(input("enter a number to guess:"))#guess integer value only
            attempts+=1
            if(guess>guess_number):
                print("the number is too high")
            elif(guess<guess_number):
                print("The number is too low")
            else:
                print("your guess is correct")
                break  
        except ValueError:
            print("enter valid number")
guess_number()