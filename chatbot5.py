def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))
def remind_name():
    print('\nPlease, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))
def guess_age():
    print('\nLet me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {0}; that's a good time to start programming!".format(age))
def number_guess():
    import random
    import math
    print("\nHey! Here's a number guessing game for you!")
    lower = int(input("\nEnter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
          round(math.log(upper - lower + 1, 2)),
          " chances to guess the integer!\n")
    count = 0
    while count < math.log(upper - lower + 1, 2):
        count += 1
        guess = int(input("Guess a number:- "))
        if x == guess:
            print("Congratulations you did it in ",
                  count, " try")
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")
def count():
    print('\nNow I will prove to you that I can count to any number you want.')
    num = int(input())
    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1
def test():
    print("\nLet's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
    print('Completed, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
greet('Bhagvat Mutthe', '2023')
remind_name()
guess_age()
number_guess()
count()
test()
end()