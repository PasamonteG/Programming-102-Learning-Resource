# Simulation of two dice being rolled
import random

# Creation of a die function. I need two we can call the function twice
def roll_dice():
    numbers = [1,2,3,4,5,6]
    result = random.choice(numbers)
    return result
#--------------------------------------------------------------------------------------#

# Build function with two dice and registering the score
def two_dice_roll(n):
    '''
    This is a strange function which will roll two dice and register the numbers
    of occurrences after n-rolls.
    The argument is the number of times to roll both dice.
    '''
    # This list stores the scores of each roll
    score = []

    # Rolling argument-times
    for i in range(n):
        # Roll both dice and sum the results
        die_1 = roll_dice()
        die_2 = roll_dice()
        sum_both = die_1 + die_2
        # Store the sum in our score list
        score.append(sum_both)
    return score

#--------------------------------------------------------------------------------------#

# We now need a function to compare the result of rolling both dice and return the number of occurrences
def result_histogram(l):
    '''
    Function to count the number of occurences in a list.
    The argument is a list
    '''
    # another list to store the number of occurrences in the members of the list
    occurrences = list(set(l))

    # finally the histogram of the occurrences
    histogram = []
    for i in occurrences:
        histogram.append(l.count(i))

    # for the sake of understanding the function returns both the occurrences and the histogram
    # in ascending order of the occurrences
    return occurrences,histogram

#--------------------------------------------------------------------------------------#

roll_number = int(input('Times to roll both dice: '))

# Running of the function to roll two dice. The result is the list of the scores
dice_out = two_dice_roll(roll_number)
print('Result of rolling both dice',dice_out)

# Finally two lists: the scores in ascending order and the corresponding occurrences
print(result_histogram(dice_out))
