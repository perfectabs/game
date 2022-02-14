from random import randint 
secret = randint(1, 1000) 
print("Welcome!") 
guess = 0 
while guess != secret: 
    g = input("Guess the number: ") 
    guess = int(g) 
    if guess == secret: 
        print("You win!") 
    else: 
        if guess > secret: 
            print("Too high") 
        else: 
            print("Too low") 
print("Game over!")
print("continue game?")
do = input("choose yes or no")
if do == "yes":
    print("ok we'll continue")
else:
        print("game over again, sorry")
        
