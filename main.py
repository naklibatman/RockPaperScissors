import random

# Rock paper Scissors game:-

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
rps_list = [rock, paper, scissors]
choose = int(input("What do you want to choose? Type 0 for Rock, Type 1 for Paper and Type 2 for scissors. \n"))
print("You Chose :- \n")
print(rps_list[choose])
print("Computer Choose :- \n")
c_choose = random.randint(0, 2)
print(rps_list[c_choose])
if choose == c_choose:
    print("It is a Tie.")
elif choose != c_choose:
    if choose == 0:
        if c_choose == 1:
            print("You Win!!!")
        else:
            print("You Loose!!!")
    elif choose == 1:
        if c_choose == 0:
            print("You Win!!!")
        else:
            print("You Lose!!!")
    elif choose == 2:
        if c_choose == 1:
            print("You Win!!!")
        else:
            print("You Loose!!!")







