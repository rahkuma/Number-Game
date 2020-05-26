import random

attempt = 1
while True:

    random_number = int(input('Enter a random number between 1 to 10... :'))
    print(f'the number you entered is {random_number}')
    num = random.randint(1, 10)
    print(f'the random number is {num}')
    if num == random_number:
        print("wooooo... correct guess")
        print(f'You completed in {attempt} attempt')
        break
    else:
        print("Sorry wrong guess.... give one more try")
        attempt += 1