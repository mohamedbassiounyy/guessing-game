import random

attempts_list =[]

def show_score():
    if not attempts_list:
        print("No scores yet")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")


print("Welcome to the guessing game. ")
player_name = input("What's your name? ")
wanna_play = input(
    f"Hello {player_name}, Are you ready to play! "
    "(Enter Yes/No) ").lower().strip()
if wanna_play == "yes":
    print("Well, Let's play!")
else:
    print("Okay, see you later!")
    exit()
while wanna_play == "yes":
    attempts = 0
    rand_number = random.randint(10, 20)
    show_score()
    while True:
        try:
            guess = int(input("Guess a number between 10 to 20: "))
            if (guess < 10 or guess > 20):
                print("Please guess a number within the given range.")            
                continue
            attempts += 1

            if(guess == rand_number):
                print(f"Congratulations! {player_name} Let's do it again.")
                print(f"You got it in {attempts} attempts")
                attempts_list.append(attempts)
                break
            elif(guess < rand_number):
                print("Your guess is lower! ")
            else:
                print("Your guess is higher! ")
            

        except ValueError as err:
            print(err)
    
    wanna_play = input("Would you like to do it again? "
                                "(Enter Yes/No): ")
    if wanna_play != "yes":
        print("Have a nice day!")
exit()
    
    
