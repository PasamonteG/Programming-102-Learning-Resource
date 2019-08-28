## Guessing Game

max = 101
min = 0

print("Think of a number between 1 and 100")

# We use mostly the same function as before.
# The function is slightly modified to fit in the while loop by setting the running variable to False
# and break the infinite loop.
def guess_number(min,max):
    running = True
    while running:
        middle = int((max + min)/2)
        answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
        if answer == "H":
            min = middle
        elif answer == "L":
            max = middle
        else:
            print("Your number is {}, it took me 1 guess".format(middle))
            running = False
            #quit()

# Also the new thing here is to use a function to run the program. Java style.
def main():
 guess_number(min,max)

main()
