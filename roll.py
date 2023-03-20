# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import random


#  - roll a "die" some number of times.
# roll - run it once and go into a loop
#  - roll 1 - produce a number 1-6 random and print it
#  - roll 2 - produce two numbers 1-6 and print them
# - roll 3 - produce three numbers and print them.
#

def randnum():
    return random.randint(1, 6)

def test_randnum(n):
    for _ in range(n):
        t = randnum()
        if not (t >= 1 and t <=6):
            print('FAILED')
            return
    print(f"Tested {n} times. Works!")

def do_it_again():
    user_answer = input("Roll Again? (1 for yes, 2 for no) ")
    if user_answer == '1':
        return True
    else:
        return False

def test_do_it_again():
    t = do_it_again()
    print(t)

def roller():
    roll(1)
    while True :
        if do_it_again() == True:
            roll(1)
        else:
            break # leave loop and done.

def roll(n):
    # test_randnum(100)
    for i in range(n):
        print(randnum())

print("roll 1")
roll(1)
print("roll 2")
roll(2)
print("roll 3")
roll(3)

print("roller!!")
roller()
# test_do_it_again()
