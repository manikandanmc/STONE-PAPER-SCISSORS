rock ='''
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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user_input=int(input("what do you like to select rock-0 paper-1 scisscor-2\n"))
if user_input >=3 or user_input <0:
  print("invalid input")
else:
  image=[rock,paper,scissor]
  print("your input\n",image[user_input])
  com_input=random.randint(0,2)
  print("computer input\n",image[com_input])
  if user_input==0 and com_input==2:
    print("YOU WON")
  elif com_input==0 and user_input==2:
    print("COMPUTER WON")
  elif user_input > com_input:
    print("YOU WON")
  elif com_input > user_input:
    print("COMPUTER WON")
  elif com_input==user_input:
    print("Game draw")
  
    