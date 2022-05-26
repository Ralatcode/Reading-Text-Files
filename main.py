# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

# from tkinter import W


def read_file_content(filename):
    # [assignment] Add your code here
     
    # using the read() method and 
    # closing the file automatically with the "with" statement
    with open('./story.txt') as story:
        contents = story.read()
    # returns the read text in the file as a string
    return contents

print("Task 2: \nThis is the text read from the file: \n",read_file_content('./story.txt'))

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    # First, we split our string using split()
    split_text = text.split(" ")

    # we create a dictionary and store it in variable text_dict
    text_dict = dict()

    # loop through each word and add one to the value if the word repeats, else print one
    for word in split_text:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1

    # return our dictionary with words as keys and values as count.
    return text_dict

print("\nTask 3: \nThis is the dictionary returned from the read text: \n",count_words())