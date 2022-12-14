import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_playing = "_" * len(word)
    guessed = False
    guessed_words = []
    guessed_letters = []
    lives = 6
    """
    Display welcoming
    """
    print("WELCOME TO")
    # Title ASCII ART
    print(" ██░ ██  ▄▄▄       ███▄    █  "
          " ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ ")
    print("▓██░ ██▒▒████▄     ██ ▀█   █  "
          "██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ")
    print("▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒"
          "██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒")
    print("░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░"
          "▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒")
    print("░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░"
          "▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░")
    print(" ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  "
          "░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ")
    print(" ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░"
          "  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░")
    print(" ░  ░░ ░  ░   ▒      ░   ░ ░ "
          "░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ ")
    print(" ░  ░  ░      ░  ░         ░  "
          "     ░        ░         ░  ░         ░ ")
    print("\n")
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print(word_playing)

    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_playing)
                indices = [
                    i for i,
                    letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_playing = "".join(word_as_list)
                if "_" not in word_playing:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_playing = word
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_playing)
        print("\n")
    if guessed:
        print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗")
        print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║")
        print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║")
        print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝")
        print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗")
        print("   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝")
        print("Congrats, you guessed the word! You win!")
    else:
        print(" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗")
        print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
        print("██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
        print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
        print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
        print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
        print("Sorry, you ran out of lives. The word was " + word + ". Maybe next time!")


def display_hangman(lives):
    body_parts = [  # final body: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return body_parts[lives]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)       
    print("Goodbye!")
    print("_____________________________________________________________")
    print("      __                                                   /")
    print("    /    )                      /    /                    /")
    print("---/----------__-----__-----__-/----/__------------__----/---")
    print("  /  --,    /   )  /   )  /   /    /   )  /   /  /___)  / ")
    print("_(____/____(___/__(___/__(___/____(___/__(___/__(___ __o_____")
    print("                                            /                ")
    print("                                        (_ /                 ")


if __name__ == "__main__":
    main()
