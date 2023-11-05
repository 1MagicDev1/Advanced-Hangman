import random


def hangman():
    # Initialise variables including how many lives before the game ends
    mistakecounter = 0
    randomword = ''
    emptyplaces = []

    charlist = []
    usedletters = []

    # Make a while loop to add the amount of underscores to how many letters there are
    def makeEmptyLetters():
        for i in range(howmanyletters):
            if charlist[i] == '-':
                emptyplaces.append('-')
            else:
                emptyplaces.append('_')
        for index in emptyplaces:
            print(index, end=" ")

    # Print the empty places
    def printCurrentLetters():
        for i in range(len(emptyplaces)):
            print(emptyplaces[i], end=" ")

    # Ask the user for their guess and make it lower case and make sure the answer is valid otherwise react accordingly
    def useranswer():
        guess = input("\nGuess: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please answer with one character between the letters A and Z")
            return ''
        if 'a' <= guess <= 'z':
            if guess in usedletters:
                print("You have already used that letter, please use a different one!")
                return ''
            usedletters.append(guess)
            return guess
        print("Please answer with one character between the letters A and Z")
        return ''

    # Check if there are any letters in the inputare equal to any letters in the word and return all the indexes in which they appear
    def checkanswer(answered):
        outputs = []
        for i in range(len(randomword)):
            if randomword[i] == answered:
                outputs.append(i)
        return outputs

    # Open, read and split the words into the list 'words'
    with open('Hangman words.txt') as hangman_word_document:
        contents = hangman_word_document.read()
        words = contents.split()

    # Pick a random word and add it to the str variable 'randomword'
    gameRunning = True
    randomword = random.choice(words)
    # print(randomword)
    # Add each individual letter into a list called 'charlist'
    for char in randomword:
        charlist.append(char)

    # Identify how many letters there are in the letter and assign it to the variable 'howmanyletters'
    howmanyletters = len(charlist)

    # Print the name 'HANGMAN'
    print("----------HANGMAN----------")
    lives = 0
    while gameRunning:
        livesInput = input("How many lives would you like?: ")
        if livesInput.isdigit() and int(livesInput) > 0:
            lives = int(livesInput)
        else:
            print("Please enter a valid number greater than 0.")

        # Refer to the function 'makeEmptyLetters'
        makeEmptyLetters()

        # Start the loop of the game by initiating the variable that the game hasn't been won yet
        win = False

        # While the game has not been won yet or the user has not run out of lives, keep the game running
        while not win and lives > 0:
            # Set the variable to the answer given by the user
            answer = useranswer()
            # Check if the answer is valid and correct, if not, refer to the 'useranswer' and 'checkanswer' functions
            # and have it react accordingly to the rules of hangman with configurable lives initialised at the top of the code
            if len(answer) == 1:
                output = checkanswer(answer)
                if len(output) == 0:
                    print("The letter you have answered is not part of this word, please try again!")
                    lives -= 1
                    mistakecounter += 1
                    if lives == 1:
                        print("\nYou have " + str(lives) + " life left!")
                    else:
                        print("\nYou have " + str(lives) + " lives left!")
                else:
                    for i in output:
                        emptyplaces[i] = randomword[i]
                    win = True
                    for i in range(len(emptyplaces)):
                        if emptyplaces[i] == '_':
                            win = False
                            break
                printCurrentLetters()

        # If you have run out of lives, you lose, print out the word that they were trying to guess
        # If they win, congratulate them and print out how many mistakes they made, if any
        if lives == 0:
            print("\nYou've run out of lives...'")
            print("\nThe word you were trying to guess was '" + randomword + "'")
        elif win:
            if mistakecounter > 1:
                print("\nYou won with " + str(mistakecounter) + " mistakes!")
            elif mistakecounter == 1:
                print("\nYou won with only " + str(mistakecounter) + " mistake!")
            else:
                print("\nCongrats! You won without making a single mistake!")
        gameRunning = False


def addnewwords():
    def checkcopies(oldwords, addedwords):
        different_words = []
        same_words = []
        for word1 in oldwords:
            found_match = False
            for word2 in addedwords:
                if word1 == word2:
                    same_words.append(word1)
                    addedwords.remove(word1)
                    found_match = True
                    break

            if not found_match:
                different_words.append(word1)

        for word in addedwords:
            if word not in different_words:
                different_words.append(word)
        return {"same_words": same_words, "different_words": different_words}

    with open('Hangman words.txt') as hangman_word_document:
        contents = hangman_word_document.read()
        currentwords = contents.split()

    newwords = input(
        "What new words would you like to add to the list (use '-' if there are any spaces in the answer and seperate each word with a space)\nYour new words: ").lower()
    newwords = newwords.split()

    words = checkcopies(currentwords, newwords)

    with open('Hangman words.txt', 'w') as hangman_word_document:
        hangman_word_document.write(' '.join(words["different_words"]))

    if len(words["same_words"]) == 1:
        print("You already have the word:\n")
        for word in words["same_words"]:
            print(word)
    elif len(words["same_words"]) > 1:
        print("You already have the words:\n")
        for word in words["same_words"]:
            print(word, end=" ")

    if len(words["different_words"]) == 1:
        print("\nYou have added the word:\n")
        for word in words["different_words"]:
            print(word)
    elif len(words["different_words"]) > 1:
        print("\nYou have added the words:\n")
        for word in words["different_words"]:
            print(word, end=" ")


def removewords():
    def checkcopies(oldwords, removingwords):
        different_words = []
        same_words = []
        for word1 in oldwords:
            found_match = False
            for word2 in removingwords:
                if word1 == word2:
                    same_words.append(word1)
                    removingwords.remove(word1)
                    found_match = True
                    break

            if not found_match:
                different_words.append(word1)

        for word in removingwords:
            if word not in different_words:
                different_words.append(word)
        return {"same_words": same_words, "different_words": different_words}

    with open('Hangman words.txt') as hangman_word_document:
        contents = hangman_word_document.read()
        currentwords = contents.split()

    wordsToBeRemoved = input(
        "What words would you like to remove? (if there are multiple, please separate them with a space)").lower()
    wordsToBeRemovedList = wordsToBeRemoved.split()

    words = checkcopies(currentwords, wordsToBeRemovedList)

    if len(words["same_words"]) > 0:
        for word in words["same_words"]:
            currentwords = [w for w in currentwords if w != word]

        with open('Hangman words.txt', 'w') as hangman_word_document:
            hangman_word_document.write(' '.join(currentwords))

    words["different_words"] = [word for word in wordsToBeRemovedList if word not in currentwords]

    if len(words["same_words"]) > 0:
        if len(words["same_words"]) == 1:
            print("You have removed the word:\n")
        else:
            print("You have removed the words:\n")
        for word in words["same_words"]:
            print(word, end=" ")

    if len(words["different_words"]) > 0:
        if len(words["different_words"]) == 1:
            print("\nThe following word does not exist in the Hangman word list:\n")
        else:
            print("\nThe following words do not exist in the Hangman word list:\n")
        for word in words["different_words"]:
            print(word, end=" ")
    print("\n")


def listwords():
    with open('Hangman words.txt') as hangman_word_document:
        words = hangman_word_document.read()
        print("All words: \n" + words + "\n")


while True:
    startgame = input("Please make a selection\n1: Play Hangman\n2: Edit the word list\n3: Exit\nYour selection: ")
    if startgame == '1':
        hangman()
    elif startgame == '2':
        while True:
            startgame2 = input(
                "How would you like to edit the word list?\n1: List all words\n2: Add new words\n3: Remove words\n4: Go back to main menu")
            if startgame2 == '1':
                listwords()
            elif startgame2 == '2':
                addnewwords()
            elif startgame2 == '3':
                removewords()
            elif startgame2 == '4':
                print("\nBack to main menu!\n")
                break
            else:
                print("\nPlease enter a valid selection\n")
    elif startgame == '3':
        print("Goodbye!")
        exit()
    else:
        print("Please enter a valid selection\n")
