import random

play1 = input("Enter your choice (rock/paper/scissors): ").capitalize()
play2= random.randint(1,3)


if play2==1:
    play2 = "rock"
elif play2 ==2:
    play2 ="paper"
elif play2 ==3:
    play2 ="scissors"

print("computer:",play2)


if  play1== play2:
    print("its a tie")  
elif(play1 =="rock" and play2 =="scissors") or (play1 =="paper" and play2 =="rock") or (play1 =="scissors" and play2 =="paper"):
  print("you win")
else:
   print("you lose")

