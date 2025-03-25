import random
random.randint(1,100)
jackpot=random.randint(1,100)
guess=int(input("guess kor number eta"))
while guess!=jackpot:
    if guess > jackpot:
        print("guess lower")
    
    else:
        print("guess higher")
    guess=int(input("akou try kor"))    
print("right guess")    