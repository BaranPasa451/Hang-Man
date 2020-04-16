from random import randint


def open_file ():
#C:/Users/baran/OneDrive/Documents/Words_for_hangman
    text_file = open("C:/Users/baran/OneDrive/Documents/Words_for_hangman.txt", "r").read().splitlines()
    return text_file[randint(0,len(text_file)-1)]


def right_letter (letter, fill_list, word_letter, fill_words):
    check = False
    for index, item in enumerate(word_letter):
        if item == letter:
            fill_list[index] = letter
            check = True
    if not check and letter not in fill_words:
        fill_words.append(letter)
    return check

#For creating underscore list to fill with right letters
def create_fill (fill_list, word_letter):
    for item in word_letter:
        fill_list.append("_")

remaing_tries = 6 #number of tries
word = open_file()
fill_list = [] #empty list for underscores
word_letter = list(word) #list of word characters
#print(word_letter)
fill_words = [] #incorrect letters

create_fill(fill_list, word_letter)
while True:
    print(" ".join(fill_list))
    print(",".join(fill_words))
    print("You have ", remaing_tries - len(fill_words), " tries left")
    if remaing_tries == len(fill_words):
        print("You have run out of tries, goodbye")
        break
    user_input = input("What is your letter?")
    if len(user_input) == 1 and user_input.isalpha():
        right_letter(user_input, fill_list, word_letter, fill_words)
    else:
        print("Must be one letter!")
    if word_letter == fill_list:
        print("You win!")
        break


