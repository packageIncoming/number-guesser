#First, get the difficulty the player wants, easy is 1-10, medium is 1-50, and hard is 1-100
import random
difficulty = input("What difficulty would you like to play on? EASY for numbers 1-10, MEDIUM for numbers 1-50, and HARD for numbers 1-100 \n")

d = {
  "easy":10,
  "medium":50,
  "hard":100
}

maxnum = d.get(difficulty.lower(),10)

string = "Guess what number I am thinking about..."

guess = int(input(string))

chosen = random.randrange(1,maxnum+1)

score = 100

while guess != chosen:
  print("You got it wrong!")
  if guess > chosen:
    print("You went over my number.")
    if chosen*2 < guess:
      print("You went over double my number!")
  elif guess < chosen:
    print("You went under my number.")
    if guess > chosen*2:
      print("You went over double my number!")
  guess = int(input(string))
  score = score - ((1/maxnum)*100)
  if score <= 0:
    break

if guess == chosen: # Got it right
  print("You got it right! The answer was {}, and you got a score of {}%".format(chosen,score))
else: # Got it wrong
  print("Too bad. You failed! The correct number was {}".format(chosen))
