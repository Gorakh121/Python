import random

def number_guess ():
    number_to_guess = random.randint(1,100)
    number_of_attempt = 0
    guess = None
    
    print("WELCOME TO NUMBER GUESSING GAME")
    print("I'm thinking between 1 to 100 you have to guess that number")
    
    while guess != number_to_guess:
        try:
            guess= int(input("Enter your guess:"))
            number_of_attempt +=1
            
            if guess < number_to_guess:
                print("to low")
                
            elif guess> number_to_guess:
                print("to high")
                
            else:
                print("congratulatiion")
                
        except:
            print("please enter the valid number")
            

number_guess()