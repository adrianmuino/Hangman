from random import randint

# State variables
player = None
secret_word = None
letters_guessed = None
wrong_guesses = None
mistakes_made = None
max_guesses = 6

# Generates and returns a random word
def generate_word():
    file = open('words.txt','r')
    word_bank = file.read().split()
    random_int = randint(0,len(word_bank)-1) #generating random index
    random_word = word_bank[random_int]
    file.close()
    return random_word

# Prints and formats the interface of a game
def print_game(letters_guessed, wrong_guesses, secret_word, lives):

    # list of each letter guessed and a '_' if the letter is not guessed
    guessed = [l if l in letters_guessed else '_' for l in secret_word]

    # list guessed converted to a string
    guessed = ' '.join(guessed)

    print('-----------------------------------------------------------------\n')
    print('{}   {}   lives = {}\n'.format(guessed, wrong_guesses, lives))

# Requests and checks user input
def get_letter():
    user_input = input('Enter a letter: ')
    if len(user_input) != 1 or not user_input.isalpha():
        print('Invalid input. Input needs to be a letter.')
        return None
    else:
        return user_input.lower()

# Begins a single game
def play():
    letters_guessed = []
    wrong_guesses = []
    secret_word = generate_word()
    mistakes_made = len(wrong_guesses)

    end_game = False
    lives = max_guesses - mistakes_made

    while(not end_game):
        print_game(letters_guessed, wrong_guesses,secret_word, lives)

        user_input = get_letter()

        if user_input == None:
            continue

        if user_input not in letters_guessed and user_input not in wrong_guesses:
            wrong_guesses.append(user_input) if user_input not in secret_word else letters_guessed.append(user_input)
        else:
            print('You already guessed this letter. Try again.')

        lives = max_guesses - len(wrong_guesses)
        guessed_word = True if len(letters_guessed) == len(secret_word) else False

        end_game = False if lives > 0 and not guessed_word else True

    print('\n')

    secret_word = ' '.join(secret_word)
    message = 'Congratulations winner!' if lives else "You're such a loser!"
    print(secret_word + '   '  + str(wrong_guesses) + '   ' + message)

# Main game function

print('Welcome to Hangman!')
player = input('Enter your name to play: ')
print('\n')
print('Hello ' + player + '!')
print('Let the fun begin.')

quit = False
while not quit:
    play()
    play_again = input('Would you like to play again? (Enter yes or no): ')
    play_again = play_again.lower()

    while play_again != 'yes' and play_again != 'no':
        play_again = input('Please Enter yes or no: ')
        play_again = play_again.lower()
    quit = True if play_again == 'no' else False
