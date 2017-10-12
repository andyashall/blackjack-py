from random import shuffle

deck = (list(range(1,11)) + ['Ace', 'King', 'Queen', 'Jack']) * 4
dealerHand = []
playHand = []

def main():
  shuffle(deck)
  addCard(dealerHand)
  addCard(playHand)
  game()

def game():
  if evalHand(playHand):
    if evalHand(dealerHand):
      print(f'Dealers hand: {printHand(dealerHand)}')
      print(f'Your hand: {printHand(playHand)}')
      action = input('Hit or Stick: ')
      if str.lower(action) == 'hit':
        playDealer(dealerHand)
        addCard(playHand)
        game()
      elif str.lower(action) == 'stick' or 'stay':
        justDealer()
        if evalHand(dealerHand):
          declareWinner(handValue(dealerHand), handValue(playHand))
        else:
          print(f'Dealer busted. Dealers hand: {handValue(dealerHand)}')
      else:
        game()
    else:
      print(f'Dealer busted. Dealers hand: {handValue(dealerHand)}')
  else:
    print(f'You busted. Your hand: {handValue(playHand)}')

def playDealer(d):
  if handValue(d) < 17:
    addCard(dealerHand)

def justDealer():
  if handValue(dealerHand) < 17:
    addCard(dealerHand)
    justDealer()

def declareWinner(d, p):
  if d > 21:
    print(f'Dealer busted. Dealers hand: {d}')
  if d == p:
    print(f"It's a tie! Dealers hand: {d}, Your hand: {p}")
  elif d > p:
    print(f'Dealer wins! Dealers hand: {d}, Your hand: {p}')
  else:
    print(f'You win! Dealers hand: {d}, Your hand: {p}')

def addCard(hand):
  deck.pop(0)
  return hand.append(deck[0])

def cardValue(card):
  if isinstance(card, int):
    return card
  elif card is 'Ace':
    return 11
  elif card is 'King' or 'Queen' or 'Jack':
    return 10

def handValue(hand):
  v = 0
  for x in hand:
    v += cardValue(x)
  return v

def printHand(hand):
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