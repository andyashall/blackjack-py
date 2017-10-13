from random import shuffle

deck = (list(range(2,11)) + ['Ace', 'King', 'Queen', 'Jack']) * 4

def main():
  shuffle(deck)
  ph, d = addCard([], deck)
  dh, d1 = addCard([], d)
  game(d1, dh, ph)

def game(d, dh, ph):
  if evalHand(ph):
    if evalHand(dh):
      print(f'Dealers hand: {printHand(dh)}')
      print(f'Your hand: {printHand(ph)}')
      action = input('Hit or Stick: ')
      if str.lower(action) == 'hit':
        dh1, d1 = playDealer(dh, d)
        ph1, d2 = addCard(ph, d1)
        game(d2, dh1, ph1)
      elif str.lower(action) == 'stick' or 'stay':
        d1, ph1, dh1 = justDealer(d, ph, dh)
        if evalHand(dh1):
          declareWinner(handValue(dh1), handValue(ph1))
        else:
          print(f'Dealer busted. Dealers hand: {handValue(dh)}')
      else:
        game(d, dh, ph)
    else:
      print(f'Dealer busted. Dealers hand: {handValue(dh)}')
  else:
    print(f'You busted. Your hand: {handValue(ph)}')

def playDealer(dh, d):
  if handValue(dh) < 17:
    return addCard(dh, d)

def justDealer(d, ph, dh):
  if handValue(dh) < 17:
    dh1, d1 = addCard(dh, d)
    return justDealer(d1, ph, dh1)
  else:
    return (d, ph, dh)

def declareWinner(d, p):
  if d > 21:
    print(f'Dealer busted. Dealers hand: {d}')
  if d == p:
    print(f"It's a tie! Dealers hand: {d}, Your hand: {p}")
  elif d > p:
    print(f'Dealer wins! Dealers hand: {d}, Your hand: {p}')
  else:
    print(f'You win! Dealers hand: {d}, Your hand: {p}')

def addCard(h, d):
  d.pop(0)
  h.append(d[0])
  return (h, d)

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

if __name__ == "__main__":
  main()