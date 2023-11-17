import random

# using 'random.randint(n, n)' function 
n = random.randint(1, 10)
guess = int(input("Enter your number: "))

while n != guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter your number: "))
    elif guess > n:
        print("Too High")
        guess = int(input("Enter your number: "))
    else:
        break
print("Correct Guess")