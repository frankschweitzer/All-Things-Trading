import random

board = ""
boardOutlook = []
  
  
def words():
  wordList = ["turtle", "gorilla", "hippo", "zebra"]
  randomWord = random.choice(wordList)
  return randomWord


def printBoard(word):
  print("This is the board")
  global board, boardOutlook
  board = ""
  i = 0
  for char in word:
    if boardOutlook[i]:
      board += char+" "
    else:
      board += "_ "
    i = i+1
  return board


gameFinished = False
gameWord = words()
boardOutlook = [False] * len(gameWord)
print(printBoard(gameWord))
while (gameFinished!=True):
  gameFinished = True
