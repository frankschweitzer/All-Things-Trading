import random

def game():
  print("Game Starting")
  gameWord = words()
  print(printBoard(gameWord))
  
  
  
def words():
  wordList = ["turtle", "gorilla", "hippo", "zebra"]
  randomWord = random.choice(wordList)
  return randomWord


def printBoard(word):
  print("This is the board")
  board = ""
  for char in word:
    board += "_ "
  return board


game()
