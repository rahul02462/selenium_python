import random
def guess_number():
    number = random.randint(1,100)
    attempts = 0

    print("welcome to number guessing game")
    while True:
        guess = int(input('enter the first number'))
        attempts+=1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print('Congratulation you have selected correct number of series!!!')
            break

        play_again = input("Do you want to play again???Yes/No")
        if play_again.lower() == 'Yes':
            guess_number()
        else:
            print("Thank you for playing..!")

guess_number()