n = 18
guess = 1
print("***************** You have only 9 guesses to win *****************")
while (guess<=9):
    guess_num = int(input("Enter Your Guess :\n"))
    if guess_num>18:
        print("You Entered number is Greater..!")
    elif guess_num<18:
        print("You Entered number is Lesser..!")
    else:
        print("You won..!")
        print(guess,"guesses you took to finish..!")
        break
    print(9-guess,"no. of guesses left\n")
    guess += 1


print("Game Over..!")

