'''
                                           --- HANGMAN ---
    Hangman game developed in python using a list of stored words. Random imported to generate random 
    word from string list. One player version with 6 lives. Hangman visualisation on terminal also implemented. 
    Short and sweet !!
'''

import random
from words import words
import string


def valid_word(words):
    word = random.choice(words)  # randomly chooses an item(word) from the list
    while '-' in word or ' ' in word:  # remove - and space ' ' words
        word = random.choice(words)

    return word.upper()  # return valid word

def hangman():
    word = valid_word(words)
    word_letters = set(word)  # to identify letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()  # store players guessed letters

    lives = 6
    print("Play Hangman!!!")

    while len(word_letters) > 0 and lives > 0:
        print(display_hangman(lives))
        print("Lives:",lives, "\nYou have guessed: ", ' '.join(guessed_letters))  # show guessed letters
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print("\nCurrent guess: ", ' '.join(word_list))
        try:
            player_guess = input("Guess a letter: ").upper()  # take the players guess
            if player_guess in alphabet - guessed_letters:
                guessed_letters.add(player_guess)  # add players guess to guessed letters if its in the alphabet/not already a guess
                if player_guess in word_letters:
                    word_letters.remove(player_guess)  # if the guess is in the word remove it from being a choice
                    print("Yup '{}' is in the word!".format(player_guess))
                else:
                    lives -= 1
                    print("'{}' is not in the word.".format(player_guess))

            elif player_guess in guessed_letters:
                print("You have already used this letter, guess again.")
        except:
            print("That's an invalid character, Please try again.")

    # loop ends here when len(word) == 0 OR lives == 0
    if lives == 0:
        print("\nNo more lives, you died!!\nThe word was", word)
        again = input("Try Again? (y/n): " )
        if again == 'y':
            return hangman()
        else:
            print("Byeeee!!")

    else:
        print("\nWell done! you got it, the word is", word)
        again = input("Play Again? (y/n): " )
        if again == 'y':
            return hangman()
        else:
            print("Byeeee!!")


def display_hangman(lives):
    ''' Display hangman stage in a list. Stages indexed by lives'''
    hangman_stages = ['''
       +---+
       |   |

       O   |

      /|\  |

      / \  |

           | 
     =========''', '''
       +---+
       |   |

       O   |

      /|\  |

      /    |

           |
     =========''','''
       +---+

       |   |

       O   |

      /|\  |

           |

           |
     =========''', '''
            +---+
       |   |

       O   |

      /|   |

           |

           |
     =========''', '''
       +---+
       |   |

       O   |

       |   |

           |

           |
     =========''', '''
       +---+
       |   |

       O   |

           |

           |

           |
     =========''','''
       +---+
       |   |

           |

           |

           |

           |
     =========''']

    return hangman_stages[lives]


hangman()
