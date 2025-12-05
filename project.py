import random # import random from the library
print("✨✨✨✨Welcome to The Guess Word Game 👾✨✨✨✨".center(100))
print()
# user choice for the level
def main():
  user_choice = input("choose the level  Easy , Medium , Hard ").lower()
  if user_choice == "easy":
      easy()
  elif user_choice == "medium":
      medium()
  elif user_choice == "hard":
      hard()
  else:
      print("Invalid choice! Please enter 'easy', 'medium', or 'hard'.")

# if user choose level easy
def easy ():
    print("Level Easy".center(100))
    # list of word for the easy level
    list_word=['car', 'egg', 'dog', 'tree', 'book']
    # hints provide for each word
    hints = {
        'car': 'You can drive it ',
        'egg': 'You can eat it for breakfast ',
        'dog': 'It says “woof woof” ',
        'tree': 'It has leaves and grows tall ',
        'book': 'You can read it '}
    # Main game loop
    for i in range(5):
    # choose a random word from the list
     secret_word= random.choice(list_word[0:5])
     # remove the current select from the list
     list_word.remove(secret_word)
     answer_format="Your answer:  " + " - " * len(secret_word)
     attempt = 3
     # display the hint to help the user
     print("Hint💡:" , hints[secret_word])
     print('word',i+1," What do you think ? ")

     # ask the user to guess the word
     user_guess = input(answer_format).lower().strip()

     # check if the guess is correct
     if user_guess == secret_word:
         print("🌟 Fantastic!...".center(50))
     print()



     while user_guess != secret_word and attempt >0:
        attempt -= 1
        if attempt>0:
            print("❌Wrong guess, try again ", attempt,"/3 attempts")
            user_guess = input(answer_format).lower().strip()
            if user_guess == secret_word:
                print("✅ Correct!".center(50))
            print()
        else:
            print("Wrong guess! 💔 Out of attempts! The word was ",secret_word)
        print()


    print("🌟 Great job! You're ready for the next level! \n", "would you like to try level medium  ?")
    user_choice= input("Yes or No ? ").lower().strip()# ask if user want to move to the next level
    if user_choice=="yes":
        medium()
    else:
        print("🏆 WELL DONE! You've completed The level ")
        print(" Thanks for playing! See you soon! 👋  ")

# if user choose level medium
def medium():
    print("Level Medium".center(100))
    # list of word for the easy level
    list_word =['apple' , 'milk' , 'home' , 'goat' , 'doctor']
    # hints provide for each word
    hints = {  'apple': "A red fruit ",
               'milk' : "A white drink ",
               'home' : "A place to live ",
               'goat' : "An animal with horns ",
              'doctor': "A person who helps sick people "}
    # Main game loop
    for i in range(5):
        # choose a random word from the list
        secret_word = random.choice(list_word[0:5])
        # remove the current select from the list
        list_word.remove(secret_word)
        answer_format = "Your answer:  " + " - " * len(secret_word)
        attempt = 4
        # display the hint to help the user
        print("Hint💡:", hints[secret_word])
        print('word',i+1," What do you think ? ")

        # ask the user to guess the word
        user_guess = input(answer_format).lower().strip()

        # check if the guess is correct
        if user_guess == secret_word:
            print("🌟 Well Done !...".center(50))
        print()

        while user_guess != secret_word and attempt > 0:
            attempt -= 1
            if attempt > 0:
                print("❌Wrong guess, try again ", attempt,"/4 attempts")
                user_guess = input(answer_format).lower().strip()
                if user_guess == secret_word:
                    print("✅ Correct!".center(50))
                print()
            else:
                print("Wrong guess! 💔 Out of attempts! The word was ", secret_word)
            print()


    print("🌟 Excellent! You're ready for the Hard level! \n", " would you like to try level hard ?")
    user_choice = input("Yes or No ? ").lower().strip()
    if user_choice == "yes":
       hard()
    else:
       print("🏆 AMAZING! You've completed The level ")
       print("  Thanks for playing! See you soon! 👋  ")

# if user choose level hard
def hard():
    print("Level Hard".center(100))
    # list of word for the easy level
    list_word = ['school', 'flower', 'mother', 'elephant', 'computer']
    # hints provide for each word
    hints = {
        'school': "A place you go to every day to learn.",
        'flower': "It grows from the ground and has nice colors and smell.",
        'mother': "The person who loves you the most and takes care of you.",
        'elephant': "A very big animal with a long nose.",
        'computer': "A device you use to play games, write, and find information."}

    # Main game loop
    for i in range(5):
        # choose a random word from the list
        secret_word = random.choice(list_word[0:5])
        # remove the current select from the list
        list_word.remove(secret_word)
        attempt = 5
        answer_format="Your answer:  " + " - " * len(secret_word)
        # display the hint to help the user
        print("Hint💡:", hints[secret_word])
        print('word',i+1," What do you think ? ")

        # ask the user to guess the word
        user_guess = input(answer_format).lower().strip()

        # check if the guess is correct
        if user_guess == secret_word:
            print("🌟 Great job!...".center(50))
        print()

        while user_guess != secret_word and attempt > 0:
            attempt -= 1
            if attempt > 0:
                print("❌Wrong guess, try again ", attempt,"/5attempts")
                user_guess = input(answer_format).lower().strip()
                if user_guess == secret_word:
                    print("✅ Correct!".center(50))
                print()
            else:
                print("Wrong guess! 💔 Out of attempts! The word was ",secret_word )
                print()


    print("🏆 AWESOME! You've completed The Hardest level!")
    print("   You're a Word Guessing Champion! 🎊")

#call the main to run the code
main()
