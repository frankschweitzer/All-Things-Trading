import random

def game():
  print("Game Starting")
  gameWord = words()
  
  
  
def words():
  wordList = ["turtle", "gorilla", "hippo", "zebra"]
  randomWord = random.choice(wordList)
  return randomWord


game()
