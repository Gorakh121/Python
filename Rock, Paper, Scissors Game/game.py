import random
rock = "rock"
paper = "paper"
scissor = "scissor" 

p = [rock, paper ,scissor]
user_Choice = int(input("Enter your choice:type 0 for rock,1 for paper, 2 for scissor:"))
print("User Choice")
print(p[user_Choice])
if user_Choice >=3 or user_Choice <0:
    print("INVALID NUMBER")
    exit
else:
    computer_Choice = random.randint(0,2)
    print("computer Choice")
    print(p[computer_Choice])

    if computer_Choice == user_Choice:
        print("draw")
    elif computer_Choice ==0 and user_Choice ==2:
        print("you loose")
    elif user_Choice ==0 and computer_Choice==2:
        print("you win")
    elif computer_Choice> user_Choice:
        print("you loose")
    elif computer_Choice< user_Choice:
        print("you won")

