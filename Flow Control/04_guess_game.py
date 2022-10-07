value=11
count=0

print("Let's, Play a game")
print("Guess a number between 1 & 20")
guess=int(input())

while(guess!=value):
    count+=1
    if(guess<value):
        print("Guess Higher")
        guess=int(input())
    elif(guess>value):
        print("Guess Lower")
        guess=int(input())

print(f"Yahh!! You guessed it correct.. in {count+1} attempt")