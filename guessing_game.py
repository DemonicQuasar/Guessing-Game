from random import randint

print('-In this game you will guess a non-decimal number number between 1 and 100.')
print('-If you are within 10 numbers of the correct number, you will be told that you are warm, and vice versa.')
print('-Starting from the second guess, you will be told how close you are to the number in relation to your past guess.')
print('-If you win, you will be told the number of guesses it took you to win.')

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

randnum = randint(1, 100)
print(randnum)
guesslist = []

while True:

    guess = input("Type a Number Between 1 and 100:")

    if is_integer(guess) == False:
        print('please type a non-decimal number between 1 and 100')
        continue

    mguess = int(guess)

    if 1 > mguess or mguess > 100:
        print('out of bounds'.upper())
        continue

    if 0 < mguess <= 100 and is_integer(guess) == True:
        guesslist.append(mguess)

    if randnum == mguess:
        if len(guesslist) == 1:
            print(f'Congratulations! Only {len(guesslist)} try'.upper())
        elif len(guesslist) > 1:
            print(f'Congratulations! Only {len(guesslist)} tries'.upper())

        while True:
            again = input('Do you want to play again? y/n').upper()
            if again == 'Y':
                randnum = randint(1, 100)
                break
            elif again == 'N':
                print('Goodbye')
                break
            else:
                continue
        continue

    if len(guesslist) == 1 and abs(randnum - mguess) <= 10:
        print('WARM!')
        continue

    if len(guesslist) == 1 and abs(randnum - mguess) > 10:
        print('COLD!')
        continue

    elif abs(randnum - mguess) >= abs((guesslist[-2]) - randnum):
        print('COLDER!')
        continue

    elif abs(randnum - mguess) <= abs((guesslist[-2]) - randnum):
        print('WARMER!')
        continue

# BRUH