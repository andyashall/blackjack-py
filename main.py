from random import shuffle

deck = (list(range(1,11)) + ['Ace', 'King', 'Queen', 'Jack']) * 4
dealerHand = []
yourHand = []

def main():
  shuffle(deck)
  dealerHand.append(deck[0])
  dealerHand.append(deck[2])
  yourHand.append(deck[1])
  print(f'Dealers hand: {handValue(dealerHand)}')
  print(f'Your hand: {handValue(yourHand)}')
  action = input('Hit or Stick: ')
  if evalHand(yourHand):
    if str.lower(action) is 'hit':
      hit(yourHand, 2)
      print(yourHand)
  

def cardValue(card):
  if isinstance(card, int):
    return card
  elif card is 'Ace':
    return 11
  elif card is 'King' or 'Queen' or 'Jack':
    return 10

def handValue(hand):
  if len(hand) is 1:
    return hand[0]
  else:
    v = 0
    for x in hand:
      v += cardValue(x)
    return v

def evalHand(h):
  v = 0
  for x in h:
    v += cardValue(x)
  if v > 21:
    return False
  else:
    return True

def hit(step, hand):
  return hand.append(deck[step])

if __name__ == "__main__":
  main()