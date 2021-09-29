import random

target_list = [random.randint(1,6) for i in range(4)]
print('The computer has generated a code')
lives = 12

def evaluate(guess, target):
    evaluation = []
    guesscopy = guess.copy()
    if guess == target:
        return 'bbbb'
    else:
        for i in range (4):
            if guesscopy[i] == target[i]:
                evaluation.append('b')
                guesscopy[i] = '_'
        for num in guesscopy:
                if num in target:
                    evaluation.append('w')
    return evaluation


while lives > 0:
    guess = input('Please enter your 4 digit guess with spaces in between: ')
    guess_list = guess.split()
    map_object = map(int, guess_list)
    guess_list = list(map_object)
    if guess_list != target_list :
        print('That is not correct')
        print('Your evaluation is: ')
        print(evaluate(guess_list, target_list))
        lives -= 1
    else:
        print('That is correct!')
        exit()
print('You ran out of lives!')
exit()