import random

num_digits =  3
max_guesses = 10

def main():
         
        print('''Bagels, a deductive logic game. By Al Sweigart al@inventwithpython.com
 I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(num_digits))
         
        while True:
                secretNum = getSecretNum()
                print('I have thought up a number.')
                print(f'You have {max_guesses} guesses to get it.')

                numGuesses = 1
                while numGuesses <= max_guesses:
                        guess = ''
                        while len(guess) != num_digits or not guess.isdecimal():
                                print(f'Guess # {numGuesses} ')
                                guess = input('> ')
                        clues = getClues(guess, secretNum)
                        print(clues)
                        numGuesses += 1

                        if guess == secretNum:
                            break
                        if numGuesses > max_guesses:
                            print('You ran out of guesses.')
                            print('The answer was {}.'.format(secretNum))
                 #Ask player if they want to play again.
                print('Do you wanna play again? (yes or no)')
                if not input('> ').lower().startswith('y'):
                    break
        print("Thanks for playing")    
                  
def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.

# Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum 
def getClues(guess, secretNum):
      
      """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
      if guess == secretNum:
        return 'You got it'
      clues = []
      for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                  
                # A correct digit is in the correct place 
                clues.append('Fermi')                               
            elif guess[i] in secretNum:
                  # A correctdigit is in the incorrect place.
                  clues.append('Pico')
      if len(clues) == 0:
            return 'Bagels' # There is no correct digits at all                            
      else:
            # Sort the clues into alphabetical order so their original order
            #  # doesn't give information away.
            clues.sort()
            # Make a single strng from the list of string clues
            return ' '.join(clues)
if __name__== '__main__':
    main()
               
