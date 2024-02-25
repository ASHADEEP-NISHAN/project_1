import random as r
a=['rock','paper','scissor']
b=r.choice(a)

while True:
    c=input("enter [rock/paper/scissor]").lower()
    print("i choose::",b)
    if b==c:
        print("tie")
    elif b=='rock' and c=='paper':
        print("you win")
    elif b=='rock' and c=='scissor':
        print("you lose")
    elif c == 'rock' and b == 'paper':
        print("you lose")
    elif b == 'paper'and c=='scissor':
        print("you win")
    elif c == 'rock' and b == 'scissor':
        print("you win")
    elif c == 'paper'and b =='scissor':
        print("you lose")
    else:
        print("invalid input")


