from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to anonimus auction!")

there_are_players = True
players = []

while there_are_players:
  name = input("Welcome, to auction! What is your name? ")
  bid = int(input("What is your bid? "))

  new_player = {
    "name": name,
    "bid": bid
  }
  players.append(new_player)

  if input("Are there any other players? ").lower() == "yes":
    clear()
    there_are_players = True
  else:
    there_are_players = False

highest_bid = 0
winner = ""
for i in players:
  if i["bid"] > highest_bid:
    highest_bid = i["bid"]
    winner = i["name"]
  else:
    pass

print(f"The winner is {winner} with the highest bid of {highest_bid}")