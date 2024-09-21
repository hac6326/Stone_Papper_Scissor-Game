import random

print("SELECT ANY ONE NUMBER BETWEEN 1-3")
print("1 for stone", ",", "2 for paper", ",", "3 for scissor")
you = int(input("Enter Your No. : "))  # Convert input to integer
print(f"Your Input is : {you}")
computer = random.choice([1, 2, 3])
print(f"Computer Input is : {computer}")

# Define the winning logic
if you == computer:
    print("It's a Tie")
elif (you == 1 and computer == 3) or (you == 2 and computer == 1) or (you == 3 and computer == 2):
    print("You Win!")
else:
    print("You Lose!")
