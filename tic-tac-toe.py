'''
 Two Player Tic Tac Toe Game

'''
#  function that will create board
print('\n' + 'Welcome To Tic Tac Toe Game !' + '\n')
game_state = ['1','2','3','4','5','6', '7', '8', '9']
player_one = ''
player_two = ''
current_player = ''
from os import system
def clear():
  # _ = system('clear')
  system('clear')
def create_board():
  clear()
  print(f' {game_state[0]}   |  {game_state[1]}  |  {game_state[2]} ' )
  print('_____|_____|_____')
  print(f' {game_state[3]}   |  {game_state[4]}  |  {game_state[5]} ' )
  print('_____|_____|_____')
  print(f' {game_state[6]}   |  {game_state[7]}  |  {game_state[8]} ' )
  print('     |     |     ')
#  to start a new game
def play():
  global player_one
  global player_two
  global current_player
  global game_state
  player_one = ''

  while player_one != 'X' and  player_one != 'O':
    player_one = input('Player one, choose your marker either X or O:'+ '\n' )

  if player_one == 'X':
    player_two = 'O'
  else:
    player_two = 'X'

  current_player = player_one
  print(f' Player 1 : {player_one}')
  print(f'\n Player 2 : {player_two} \n \n')

  game_state = ['1','2','3','4','5','6','7','8','9']
  create_board()
def toggle_player(player):
  if player == 'X':
    player = 'O'
    return player
  else:
    return 'X'

def set_location(player):
  position = 0
  while True:
    try:
      position = int(input(f'\n Player {player} turn , Enter a number (1 - 9) to choose a location of your marker :'+'\n'))
    except:
      print('Whoops! That is not a number')
      continue
    else:
      if position in range(1, 10):
        break
      else:
        print("Please choose position from 1 to 9 only")
        continue
  return position

def check_horizontal():
   for i in range(0, 9, 3):
     if game_state[i] == game_state[i + 1] and game_state[i] == game_state[i + 2]:
       return True

   return False
def check_vertical():
  for i in range(0, 3):
    if game_state[i] == game_state[i + 3] and game_state[i] == game_state[i + 6]:
      return True
  return False
def check_diag_right():
  value = ""
  counter = 0
  for i in range(0, 9, 3):
    value = value + game_state[i + counter]
    counter += 1

  if value[0] == value[1] and value[0] == value[2]:
    return True
  return False

def check_diag_left():
  square = ""
  counter = 0
  for i in range(2, 9, 3):
    square += game_state[i + counter]
    counter -= 1
  return square[0] == square[1] and square[0] == square[2]

def check_for_winner():
  is_winner = check_horizontal() or check_vertical() or check_diag_left() or check_diag_right()
  return is_winner

# Start a game
def replay():
  global game_state
  global current_player
  game_start = ''

  while game_start != 'Y' and game_start != 'N':
    game_start = input('Do you want to play new game:(Y or N) ' + '\n' )
  if game_start == 'N':
    print('\n' + 'Thanks for Playing! see you later!! ')
  else:
    play()
    game_over = False
    counter = 1
    while not game_over:
      position = set_location(current_player)

      if game_state[position - 1] != 'X' and game_state[position - 1] != 'O':
        game_state[position - 1] = current_player
      else:
        while game_state[position - 1] == 'X' or game_state[position - 1] == 'O':
          position = int(input('\n' + 'Place has already been taken, please select another position: '+'\n' ))
        game_state[position - 1] = current_player

      create_board()
      current_player = toggle_player(current_player)
      counter += 1
      if counter > 9:
        print('\n' + 'Tie Game!!')
        game_over = True
        replay()
      elif check_for_winner():
        winner = toggle_player(current_player)
        print(f'\n Congratulations!! Player {winner} Wins')
        game_over = check_for_winner()
        replay()
      else:
        game_over = False


replay()















