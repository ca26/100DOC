r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [r,p,s]
#Write your code below this line 👇
import random
Choice = int(input("What do you choose 0 for Rock, 1 for paper, and 2 for Scisscors: "))
print(images[Choice])
computerchoice = random.randint(0, 2)
print(images[computerchoice])
if Choice == computerchoice:
  print("tie")
elif Choice == 0 and computerchoice==1:
  print('Computer wins')
elif Choice == 0 and computerchoice==2:
  print('You win')
elif Choice == 1 and computerchoice==0:
  print('You win')
elif Choice == 1 and computerchoice==2:
  print('Computer wins')
elif Choice == 2 and computerchoice==0:
  print('Computer wins')
elif Choice == 2 and computerchoice==1:
  print('You win')
else:
  print('Invalid choice')