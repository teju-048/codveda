import random
def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return 10  
    elif level_chosen == 'hard':
        return 5   
    else:
        return None
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose difficulty level (easy or hard): ").lower()
    attempts = set_difficulty(level)  
    if attempts is None:
        print("Invalid difficulty level. Please choose either 'easy' or 'hard'.")
        return
    answer = random.randint(1, 100)
    guessed_number = None
    while guessed_number != answer and attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guessed_number = int(input("Guess a number: "))       
        if guessed_number < answer:
            print("Your guess is too low.")
        elif guessed_number > answer:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the right number {answer}!")
            print(f"It took you {10 - attempts + 1} attempts.")
            return
        attempts -= 1
    if attempts == 0:
        print(f"You've run out of attempts. The correct number was {answer}. You lose!")

game()
