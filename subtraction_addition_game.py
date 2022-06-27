#! Python3
import random, sys, pyttsx3


def main():
    # Main game loop:
    print("Hello subtraction_addition_game!")
    while True:
        # Ask the user if he/she wants to play:
        while True:
            response = input("Would you like to play?. Please type in Yes/No.").lower()
            if response.startswith("y"):
                break
            elif response.startswith("n"):
                sys.exit("Thank you, see you next time!")
        # Ask the user for game mode(additon/subtraction):
        while True:
            print("Would you like to do some addition or substraction exercise?")
            response = input("Please type (+) for addition or (-) for substraction")
            if response == "+":
                addition()
            elif response == "-":
                subtraction()
            # Ask user if he/she wants play again:
            print("Would you like play again?")
            while True:
                response = input("Please type in Yes/No").lower()
                if response.startswith("y"):
                    break
                elif response.startswith("n"):
                    sys.exit("Thanks for playing!")


def subtraction():
    '''Doesn't take input. Create "subtraction game" -
    Creates 20 subtraction equation. User has 3 tries for each equation.
    This funciton uses pyttsx3 module to output voice warrnig.
    Program has 2 mode : easy and hard.
    In easy mode function performs subtraction from 0-50, in hard mode performs subtraction from 0-100. '''
    # Initialize pyttsx3 module
    engine = pyttsx3.init()
    # Reduce rate of speach
    engine.setProperty("rate", rate-50)
    counter = 1 # number of question
    number_of_question = 20 # variable for amount of question
    correct_answer = 0 # variable for amount of correct_answer
    # Ask the user for level:
    print("Please select level: Easy or Hard: ", end="")
    while True:
        mode = input().lower()
        if mode.startswith("e"):
            x = 50
            break
        elif mode.startswith("h"):
            x = 100
            break
        else:
            print("Incorrect input!")
    for _ in range(number_of_question):
        # The first part of equation should be always bigger than the second
        while True:
            num1 = random.randint(1, x)
            num2 = random.randint(1, x)
            if num1 > num2:
                break
        # Loop for each equation:
        for _ in range(3):
            try:
                inp = int(input(f"{counter}: {num1} - {num2} = "))
                equation = num1 - num2
                # Check correct answer:
                if equation == inp:
                    print("Correct!")
                    engine.say("Correct")
                    correct_answer += 1
                    break
                # Output for incorrect answer:
                else:
                    print("Incorrect!")
                    engine.say("Incorrect")
            except:
                print("Incorrect input")

        counter += 1
    print(f"{correct_answer} / 20")


def addition():
    '''Doesn't take input. Create "addition game" -
    Creates 20 additon equation. User has 3 tries for each equation.
    This funciton uses pyttsx3 module to output voice warrnig. '''
    # Initialize pyttsx3 module
    engine = pyttsx3.init()
    # Reduce rate of speach
    engine.setProperty("rate", rate-50)
    counter = 1 # number of question
    number_of_question = 20 # variable for amount of question
    correct_answer = 0 # variable for amount of correct_answer
    # Main equation loop:
    for i in range(number_of_question):
        while True:
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            # Max equation score should be less or equal 100:
            if (num1 + num2) <= 100:
                break
        # Loop for each equation:
        for _ in range(3):
            try:
                inp = int(input(f"{counter}: {num1} + {num2} = "))
                equation = num1 + num2
                # Check correct answer:
                if equation == inp:
                    print("Correct!")
                    engine.say("Correct")
                    correct_answer += 1
                    break
                # Output for incorrect answer:
                else:
                    print("Incorrect!")
                    engine.say("Incorrect")
            except:
                print("Incorrect input")
        counter += 1
    print(f"{correct_answer} / 20")


if __name__ == "__main__":
    main()
