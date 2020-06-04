from random import randint

print('''- In this game you will guess a number between 1 and 100.
      \n- If you are within 10 numbers of the correct number, you will be told that you are warm, and vice versa.
      \n- Starting from the second guess, you will be told how close you are to the number in relation to your past guess.
      \n- If you win, you will be told the number of guesses it took you to win.''')

randnum = randint(1, 100)
guesslist = []

while True:

    guess = int(input("Type a Number Between 1 and 100:"))

    if 1 > guess or guess > 100:
        print('out of bounds'.upper())
        continue

    if 0 < guess <= 100:
        guesslist.append(guess)

    if randnum == guess:
        print(f'Congratulations! Only {len(guesslist)} tries'.upper())
        break

    if len(guesslist) == 1 and abs(randnum - guess) <= 10:
        print('WARM!')
        continue

    if len(guesslist) == 1 and abs(randnum - guess) > 10:
        print('COLD!')
        continue

    elif abs(randnum - guess) >= abs((guesslist[-2]) - randnum):
        print('COLDER!')
        continue

    elif abs(randnum - guess) <= abs((guesslist[-2]) - randnum):
        print('WARMER!')
        continue

# BRUH