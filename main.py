from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("*******Secret Auction********")

bids = {}
cont = True

def highest_bidder(dict):
  highest_bid = 0
  for i in dict:
    bid = dict[i]
    if int(bid) > int(highest_bid):
      highest_bid = bid
      winner = i
  print(f"the winner is {winner}")


while cont:
  name = input("What's your name?\n")
  bid = input("what's your bidding price?\n$")
  bids[name] = bid
  print(bids)
  bidders = input("is there any other bidders?\n")
  if bidders == "no":
    cont = False
    print("goodbye")
  else:
    clear()

highest_bidder(bids)