import random as r
a=['rock','paper','scissor']
b=r.choice(a)

c=input("enter [rock/paper/scissor]")
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
print("i choose::",b)


