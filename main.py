from replit import clear
import random

print("Welcome to Guess the Number\n")

end = False

while not end:
  win = False
  level = input("Easy or Hard ??  ").lower()

  if level == "easy":
    attempts = 7
  elif level == "hard":
    attempts = 5

  num = random.randint(1,100)

  print(f"\nYou have {attempts} attempts")
  while attempts > 0:
    attempts = attempts - 1
    guess = int(input("\nGuess the number  "))
    if guess > num:
      print("Go Low")
    elif guess < num:
      print("Go High")
    elif guess == num:
      attempts = 0
      win = True
    print(f"You have {attempts} guess left")
  print("\n")
  if win:
    print("You won!!")
  elif not win:
    print("You ran out of guesses\nYou lost\n")
  print(f"Number was {num}")
  
  again = input("\nPlay again??\nYes or No??  ").lower()
  clear()
  if again == "yes":
    end = False
  elif again == "no":
    end = True
    print("Goodbye")




