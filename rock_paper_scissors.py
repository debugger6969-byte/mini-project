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
import random
rock_paper_scissors = [rock, scissors, paper]

random_index = random.randint(0, 2)
#print(rock_paper_scissors[random_index])

print("Welcome to Rock, Paper, Scissors! Created By Arif.")

user = int(input("what do you choose? type 0 for Rock, 1 for Scissors, 2 for Paper :\n"))

if user == 0:
    print("You choose : ")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

    if random_index == 0:
        print("Computer choose : ")
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print("It's a tie")
    elif random_index == 1:
        print("Computer choose : ")
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print("You win. Congrats!")
    elif random_index == 2:
        print("Computer choose : ")
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        print("You lose. Better luck next time :P")

if user == 1:
    print("You choose : ")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

    if random_index == 0:
        print("Computer choose : ")
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print("You lose. Better luck next time :P")
    elif random_index == 1:
        print("Computer choose : ")
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print("It's a tie")
    elif random_index == 2:
        print("Computer choose : ")
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        print("You win. Congrats!")

if user == 2:
    print("You choose : ")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

    if random_index == 0:
        print("Computer choose : ")
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        print("You win. Congrats!")
    elif random_index == 1:
        print("Computer choose : ")
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        print("You lose. Better luck next time :P")
    elif random_index == 2:
        print("Computer choose : ")
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        print("It's a tie")












