print("~~~~~~~~~~~~~~~~~~~~~~~ \nWELCOME TO HANGMAN :)\n~~~~~~~~~~~~~~~~~~~~~~~\n")

#intro for player 1
word = input("Player 1: Enter a word for Player 2 to guess: ")

#checks for invalid input
while not word.isalpha():
  word = input("You have an invalid character in your word. Please enter a word that contains only letters! ")
word = word.lower()

wordLen = len(word)
hiddenWord = list("_ " * wordLen)
counter = int(0)

guesses = input("\nPlayer 1: Enter the number of guesses (make sure it's at least 1!): ")
#checks for invalid input
while not guesses.isnumeric() or int(guesses) <= 0:
  guesses = input("Invalid input. Please try again: ")

print("\n"*30 + "                     ░░░░░░░░░░░░░░░░░░░░░▄▀░░▌\n                     ░░░░░░░░░░░░░░░░░░░▄▀▐░░░▌\n                     ░░░░░░░░░░░░░░░░▄▀▀▒▐▒░░░▌\n                     ░░░░░▄▀▀▄░░░▄▄▀▀▒▒▒▒▌▒▒░░▌\n                     ░░░░▐▒░░░▀▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒█\n                     ░░░░▌▒░░░░▒▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄\n                     ░░░░▐▒░░░░░▒▒▒▒▒▒▒▒▒▌▒▐▒▒▒▒▒▀▄\n                     ░░░░▌▀▄░░▒▒▒▒▒▒▒▒▐▒▒▒▌▒▌▒▄▄▒▒▐\n                     ░░░▌▌▒▒▀▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒█▄█▌▒▒▌\n                     ░▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▄▀█▌▒▒▒▒▒▀▀▒▒▐░░░▄\n                     ▀▒▒▒▒▌▒▒▒▒▒▒▒▄▒▐███▌▄▒▒▒▒▒▒▒▄▀▀▀▀\n                     ▒▒▒▒▒▐▒▒▒▒▒▄▀▒▒▒▀▀▀▒▒▒▒▄█▀░░▒▌▀▀▄▄\n                     ▒▒▒▒▒▒█▒▄▄▀▒▒▒▒▒▒▒▒▒▒▒░░▐▒▀▄▀▄░░░░▀\n                     ▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▄▒▒▒▒▄▀▒▒▒▌░░▀▄\n                     ▒▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▒▀▀▀▀▒▒▒▄▀\n\n                  Chester says no cheating! Don't scroll up!\n")

while int(guesses) > 0 and '_' in ''.join(hiddenWord):
  print("\nWORD: " +  ''.join(hiddenWord))
  print("You have " + str(guesses) + " more guesses!")
  player2input = input("Player 2: Guess a letter: ")
  player2input = player2input.lower()
  print("------------------------------------")

  #if player does not enter a letter 
  if not player2input.isalpha():
    print("Invalid character! Please enter letters only :)")
  
  #if player enters more than 1 letter
  elif len(player2input) != 1:
    print("Too many characters! Please only enter 1 letter at a time.")
  
  #if player guessed a letter already found in hidden word 
  elif player2input in ''.join(hiddenWord):
    print("You already guessed that letter! Guess a new letter.")

  #letter is right and replace _ appropriately
  elif player2input in word:
    print("Letter " + player2input + " was found in word, good job Player 2!")
    for letter in word:
      if player2input == letter:
        hiddenWord[counter] = letter
      counter = counter + 2
    counter = 0
  #letter does not exist in word
  else:
    print("Oh no! Letter " + player2input + " does not exist in the word.")
    guesses = int(guesses) - 1  


#results
if int(guesses) == 0 and '_' in ''.join(hiddenWord):
  print ("\n-------------------\nGame Over :( \nThe word was: " + word)
else:
  print("WORD: " + ''.join(hiddenWord))
  print("\n-------------------\nPLAYER 2 WINS :D")
