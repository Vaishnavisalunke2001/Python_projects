import random

computer=random.choice([-1,0,1])
youstr = input("Enter your choice : ")
youDict={"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"Gun"}

you=youDict[youstr]

print(f"you choose {reverseDict[you]}\nComputer choice {reverseDict[computer]}")

if(computer==you):
    print("it's a draw")

else:
    if(computer==-1 and you ==1):
        print("you win!!")
    if(computer==-1 and you ==0):
        print("you lose!!")
    if(computer==1 and you ==-1):
        print("you lose!!")
    if(computer==1 and you ==0):
        print("you win!!")
    if(computer==0 and you ==-1):
        print("you win!!")
    if(computer==0 and you ==1):
        print("you lose!!")
    else:
        print("Something went wrong")

