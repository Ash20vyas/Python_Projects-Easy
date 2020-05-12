import random

print("H A N G M A N")
while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == "exit": break
    elif choice == "play":
        words = ['python', 'java', 'kotlin', 'javascript']
        word = random.choice(words)
        set_word = set(word)
        guess = ['-' for i in word]
        typed = []
        attempt = 8
        while attempt:
            if ''.join(guess) == word: break
            print('\n'+''.join(guess))
            input_ = input("Input a letter: ")
            if len(input_) != 1:
                print("You should print a single letter")
            elif input_ in set_word:
                for i in range(len(word)):
                    if input_ == word[i]: guess[i] = input_
                set_word.remove(input_)
            elif not input_.islower():
                print("It is not an ASCII lowercase letter")
            elif input_ in typed:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                attempt -= 1
            typed.append(input_)
        if '-' in guess:
            print("You are hanged!\n")
        else:
            print("You guessed the word " + word + "!\nYou survived!\n")
