rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random as r
a=['r','p','s']
b=r.choice(a)

# c=input("enter [rock/paper/scissor]")
if b=='r':
    print(rock)
elif b=='p':
    print(paper)
else:
    print(scissors)