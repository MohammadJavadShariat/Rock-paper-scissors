import random as rand

#User and computer privileges
Score1 = 0
Score2 = 0

while (True):
    #received from the user
    person1 = input("Rock paper scissors! (Enter E to exit.)")
    
    #received from the user
    computer = rand.randint(1,3)

    #If the random number is any of the numbers, 
    #the choice of the computer will also change
    if computer == 1 :
        computer = "Rock"
    elif computer == 2 :
        computer = "paper"
    else :
        computer = "scissors"

    #If the situation is in favor of the computer, points are given to the computer.
    if person1 == "scissors" and computer == "Rock" or person1 == "Rock" and computer == "paper" or person1 == "paper" and computer == "scissors" :
        Score2 +=1
        print(f"\nMy score: {Score1}\n*****Wow!*****\nDevice score: {Score2}")
    
    #If the situation is in favor of the user, points will be given to the user.
    elif person1 == "scissors" and computer == "paper" or person1 == "paper" and computer == "Rock" or person1 == "Rock" and computer == "scissors" :
        Score1 +=1
        print(f"\nMy score: {Score1}\n*****God thank you!*****\nDevice score: {Score2}")
    #If the modes are the same, only the text will be printed
    elif person1 == computer :
        print(f"\nMy score: {Score1}\n*****equal*****\nDevice score: {Score2}")
    #Entering E will end the program
    elif person1 == "E" :
        print(f"\nMy score: {Score1}\n*****the end*****\nDevice score: {Score2}")
    else:
        #If the option is not correct
        print("The entered option is not correct.")
    
    #To end the game
    if Score1 == 5 :
        print("Evil!")
        break
    elif Score2 == 5 :
        print("Oh why...!")
        break
    elif person1 == "E" :
        break








