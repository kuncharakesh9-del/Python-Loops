import random
Secret_number =  random.randint(1,10)
Name = (input("May I know your good name please : "))
print(f"Hi {Name}, Welcome to the Guess number game. You have only three chances to guess the correct number. All the best")

flag = 1
while(flag<=3):
    flag +=1
    User_number = int(input("Guess the number between 1 and 10. : "))
    
    if(User_number <1 or User_number>10):
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    if(User_number == Secret_number):
        print("Congratulations! You guessed the correct number.")
        break

    
    
    elif(Secret_number < User_number):
        print("Too high. Try again.")
        
    elif(Secret_number > User_number):
        print("Too low. Try again.")

else:
    print("Better luck next time! You reach 3 attempts")
    print("The correct number was ", Secret_number)