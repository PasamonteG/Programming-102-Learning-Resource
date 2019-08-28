#Program to reverse a word
def reverse_word(w):
    drow = '' # We're saving the reversed characters in this variable
    for i in w: #We go through the word introduced as a parameter in the function
        drow = i + drow # This is the reversal. If we do drow + i we reproduce the string as it is.
    return drow

word = input("Introduce word: ")
print(reverse_word(word))
