import random
import time
y = 0.5
def wait():
    time.sleep(y)
print("welcome to guess the number")
wait()
print("only smart people will know how to always win")
wait()
print("lets get started")
number = random.randrange(1,101)
tries = 7
def round():
    answer = input("take a guess")
    answer2 = int(answer)
    if answer2 > number:
        print("to high")
        return
    elif answer2 < number:
        print("to low")
        return
    elif answer2 == number:
        print("you guess it")
        return
    tries -= 1
for i in range (7):
    round()



