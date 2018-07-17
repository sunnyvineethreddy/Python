import random
num = random.randint(1, 10)
while True:
    print('Guess a number between 1 and 10')
    guess = input()
    i = int(guess)
    if i == num:
        print('Your answer is Perfect!! Congratulations')
        break
    elif i < num:
               print('Your answer is low than required')
    elif i > num:
               print('Your answer is high than required')


