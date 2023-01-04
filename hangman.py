import random

board = ""
s = set()
holder = True
  
  
def words():
  wordList = ["turtle", "gorilla", "hippo", "zebra"]
  randomWord = random.choice(wordList)
  return randomWord


def printBoard(word):
  print("This is the board")
  global board
  board = ""
  for char in word:
    if char in s:
      board += char+" "
    else:
      board += "_ "
  global holder
  if "_" in board:
    holder = True
  else:
    holder = False
  return board


def play(wrd):
  letter = input("Enter a letter: ")
  global s
  while letter in s:
    letter = input("Enter a new letter you have not guessed: ")
  s.add(letter)
  print(printBoard(wrd))
  

gameWord = words()
print(printBoard(gameWord))
while (holder):
  play(gameWord)
  