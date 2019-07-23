import random
from os import system
import time


# bank account
class User_account():

  def __init__(self, money=100):
    self.money = money

  def __str__(self):
    return f'You have ${self.money} in your account.\n'

  def deposit(self, amount):
    if amount >=0:
      self.money += amount
    else:
      print("You entered invalid amount!")

  def withdraw(self, amount):
    if self.money >= amount:
      self.money-= amount
    else:
      print("You entered invalid amount!")

  def check_balance_for_bet_money(self, bet_money):
    if bet_money > 0 and self.money >= bet_money:
      print(f'You bet for ${bet_money}, you can win ${bet_money * 2} ')
      return True
    elif bet_money > 0 and self.money < bet_money:
      print("Sorry you don't have sufficient funds in your account.You can't bet for money more than you have in hands.")
      return False
    else:
      print("Sorry! you can't play with that bet money")
      return False


class Cards():

  deck = []
  suits = {'a': '♠','b':'♣', 'c': '♥', 'd': '♦'}
  ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "A": 11,"J": 10, "Q": 10, "K": 10}

  def __init__ (self,name):
    self.bet_money = 0
    self.hands = []
    self.total = 0
    self.name = name

  def create_deck(self):
    symbols = Cards.suits
    card_values = Cards.ranks
    for card in card_values:
      Cards.deck.append(f'{card}{symbols["a"]}')
      Cards.deck.append(f'{card}{symbols["b"]}')
      Cards.deck.append(f'{card}{symbols["c"]}')
      Cards.deck.append(f'{card}{symbols["d"]}')

  def picks_random_card(self):
    card = Cards.deck[random.randint(0, 51)]
    while card in self.hands:
      card = Cards.deck[random.randint(0, 51)]
    return card

  def picks_unique_cards_pair(self):
    card1 = self.picks_random_card()
    card2 = self.picks_random_card()
    while card1 == card2:
      card1 = self.picks_random_card()
    self.hands.append(card1)
    self.hands.append(card2)

  def compare_hands(self, hands):
    for card in hands:
      while card in self.hands:
        self.hands.pop(self.hands.index(card))
        new_card = self.picks_random_card()
        self.hands.append(new_card)

  def calculate_sum(self):
    points = []
    for rank in self.hands:
      points.append(Cards.rank_values[rank[: -1]])
    score = sum(points)
    if score > 21:
      for rank in self.hands:
        if rank[ :-1] == 'A':
          score-= 10
    self.total = score

  def check_for_win_or_bust(self):
    game_over = False
    game_status = 'not known'
    if self.total > 21:
      # print(f"\nYour cards total: {self.total}")
      print('\nSorry! You Busted!!')
      game_over = True
      game_status = 'lose'
    elif self.total == 21:
      print('\n' + 'Yay!! You made 21.')
      print(f"\nCongratulations!! You WON ${self.bet_money * 2}")
      game_over = True
      game_status = 'win'
    return (game_over, game_status)


class Comp_Cards(Cards):

  def calculates_comp_hits(self, player_total):
    comp_cards.calculate_sum()
    while comp_cards.total < player_total:
      card3 = comp_cards.picks_random_card()
      comp_cards.hands.append(card3)
      comp_cards.calculate_sum()

  def __str__(self):
    return f'{self.name} cards are: {self.hands[0]}  ?\n'

class Player_Cards(Cards):

  def __str__(self):
    result = f"{self.name} cards are: "
    index = 0
    for _ in self.hands:
      result+= f"{self.hands[index]} "
      index += 1
    result += f"\n\nYour card's score: {self.total}\n"
    return result

############################  helper methods  ###########################

def clear():
  system('clear')

def declare_result(game_over, game_status):
  if game_status == 'win':
    player_balance.deposit(bet_money * 2)
    print(player_balance)
  elif game_status == 'lose':
    player_balance.withdraw(bet_money)
    print(player_balance)

def start_game():
  play_game = input( 'Are you willing to play? (y / n): ')
  while play_game != 'y' and play_game != 'n':
    play_game = input('Are you willing to play? (y / n): ')
  return play_game

def ask_for_valid_bet():
  while True:
    try:
      bet_money = int(input('How much money do you want to bet for ? :\n'))
    except:
      print("Whoops!! You must enter bet money to start the game.\n ")
    else:
      player_cards.bet_money = bet_money
      break
  return bet_money

def hit_or_stay():
  response = input('Player do you want to HIT Deck ? (y / n): ')
  while response != 'y' and response != 'n':
    response = input('Invalid response! please answer in y or n: ')
  return response

def compare_scores(player_score, comp_score):
  if comp_score > 21 or player_score > comp_score:
    print('Congratulations!! You won the game.\n')
    player_balance.deposit(player_cards.bet_money * 2)
    print('\n')
    print(player_balance)
  elif player_score == comp_score:
    print("It's a TIE !! Your bet money is all yours.\n " )
    print('\n')
    print(player_balance)
  elif comp_score == 21 or player_score < comp_score:
    player_balance.withdraw(player_cards.bet_money)
    print("Sorry! You lost\n ")
    time.sleep(2)
    clear()
    print(player_balance)
    print('\n')
    print("Hey!! don't give up on your dream, you can still try your luck.\n")
    time.sleep(4)
    clear()


############################## GAME STARTS HERE ##########################

player_balance = User_account()
print('\n' + 'Welcome to Black Jack Game.Spend BIG and WIN BIG')
print('\n'+ 'Double your offer on each win!! ')
print('\n'+ 'You can be a Millionaire'+'\n')
time.sleep(2)
play = True
while play:
  play_game = start_game()
  player_cards = Player_Cards('Player')
  player_cards.create_deck()
  comp_cards = Comp_Cards('Dealer')
  comp_cards.create_deck()
  if play_game == 'y':
    clear()
    player_cards.picks_unique_cards_pair()
    comp_cards.picks_unique_cards_pair()
    ## Takes in player's hand and checks for and replaces any matching card in computer's hand with the unique one.
    comp_cards.compare_hands(player_cards.hands)
    print(f'\nYou have ${player_balance.money} in your bank right now \n')
    bet_money = ask_for_valid_bet()
    hasMoney = player_balance.check_balance_for_bet_money(bet_money)
    if not hasMoney:
      clear()
      print("You don't have sufficient funds in your account to play!!")
      time.sleep(2)
      play = False
    else:
      time.sleep(2)
      clear()
      player_cards.calculate_sum()
      print(player_cards)
      print(comp_cards)
      game_over, game_status = player_cards.check_for_win_or_bust()
      if game_over:
        declare_result(game_over, game_status)
        continue
      response = hit_or_stay()
      while response == 'y':
        picked_card = player_cards.picks_random_card()
        player_cards.hands.append(picked_card)
        player_cards.calculate_sum()
        clear()
        print(player_cards)
        print(comp_cards)
        game_over, game_status = player_cards.check_for_win_or_bust()
        if game_over:
          declare_result(game_over, game_status)
          break
        else:
          response = hit_or_stay()
          continue
      if response == 'n':
      # player wants to STAY
        total = player_cards.total
        print(f'\nYour Score is: {total}\n')
        # Now it's computer's turn: calculate and store  computer's score
        comp_cards.calculates_comp_hits(total)
        comp_total = comp_cards.total
        print(f"Dealer's Score is: {comp_total}\n ")
        compare_scores(total, comp_total)
        continue
  else:
    break
play = False
clear()
print(f'See you next time, Goodbye.')
