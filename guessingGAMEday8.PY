import random
random.randint(1,100)
jackpot=random.randint(1,100)
guess=int(input("guess kor number eta : "))
counter=1
while guess!=jackpot:
    if guess > jackpot:
        print("guess lower : ")
    
    else:
        print("guess higher : ")
    guess=int(input("akou try kor : "))
    counter+=1    
print("right guess")   
print("you took",counter,"times") 