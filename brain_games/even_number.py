import random
import prompt


def is_number_even(num):
    return num % 2 == 0


def check_number(name):
    for i in range(3):
        # Offer number and get gamer's answer
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if answer == 'yes':
            if is_number_even(number):
                print('Correct!')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                return
        elif answer == 'no':
            if is_number_even(number):
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                return
            else:
                print('Correct!')
        else:
            print(f'{answer} is not valid answer. Try again')
            return
    print(f'Congratulations, {name}!')
