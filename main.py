from art import game_art
from art import game_status
import random

print('''
$$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
$$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
$$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
$$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
$$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
\__|  \__|\________|\________|\________|\______/  
''')

P1_pnt = 0
P2_pnt = 0

print("\nWelcome to Rock, Paper ,Scissors game!")
print(f"You will play against the computer, your current point is {P1_pnt}.")

end_of_game = False

while not end_of_game:
  print("\n======================================================================")
  choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissor: "))
  cmp_choice = random.randint(1, 3)
  print(f"\nYour Choice is ", game_art[choice - 1])
  print(f"\nComputer Choice is ", game_art[cmp_choice - 1])

  #Tie case
  if cmp_choice == choice:
    print("it's a tie")
  elif (cmp_choice == 1 and choice == 3) or (
      cmp_choice == 2 and choice == 1) or (cmp_choice == 3 and choice == 2):
    #Lost case
    P2_pnt += 1
    print("You lost, computer wins this round.")
  elif (choice == 1 and cmp_choice == 3) or (
      choice == 2 and cmp_choice == 1) or (choice == 3 and cmp_choice == 2):
    #Win case
    P1_pnt += 1
    print("You won this round! Good job.")

  print(f"Your current point is {P1_pnt}, Computer points are {P2_pnt}\n")
  repeat = input(
      "Do you want to continue playing?\nType 'Yes' or 'No'").lower()
  if repeat == "no":
    end_of_game = True

#show the final result
print("\n======================================================================")
print(f"Your current point is {P1_pnt}, Computer points are {P2_pnt}\n\n")
if P1_pnt == P2_pnt:
  print(game_status[2])
elif P1_pnt > P2_pnt:
  print(game_status[0])
else:
  print(game_status[1])
