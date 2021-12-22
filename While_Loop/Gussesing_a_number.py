"""Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again until the guess is correct.
On successful guess, user will get a "Well guessed!" message, and the program will exit."""
i=0                                                      #initialse i=0
while i<=0:                                               #condition for infinite loop untill break or exit is used
    n=int(input("Guess a number between 0-9:"))           # take input from user and convert it to integer
    if n>10:
        print("More than 1 no. entered,Please Enter in range of 0-9:")
    elif n==6:                                              #this is the correct number
        print("Well Gussed!!!")
        break                                               #to break the loop
    else:
        print("Wrong guess Please Try Again")

#2nd way:
import random                                                   #importing random module

while True:                                                     #for infinite loop
    randomno=random.randint(0,9)                                    #fetching random no. form range 0 to 9
    n1=int(input("Enter a number:"))
    if randomno==n1:
        print("Correct Guess!!","The number was:",randomno)
        break                                                     #to break the loop
    else:
        print("Wrong guess..The Number was",randomno,"Try again..")