# Loading the regular expression module.

import re

# Defining a function that takes the paragraph as input and returns the sentences.

def split_into_sentences(paragraph):

# Using the pattern that matches sentences that starts with a capital letter and end with the differents marks of sentences: .,!,or ?.


    pat = r'[A-Z].*?[.!?](?= [A-Z]|$)'

# Finding all occurences ( sentences) that match the pattern. 

    sentences = re.findall(pat,paragraph)

# Sending back the list of the sentences found in the paragraph.

    return sentences

# Defining another function to print the sentences and count them.

def display_sentences(sentences):

# Looping through each sentences and adding a -> before printing them 

    for i in sentences:
        print('->', i)

# Printing how many sentences were found in the paragraph.

    print(f"\nTotal of sentences: {len(sentences)}")

# Running the executed file by prompting the user to enter the paragraph and calling the two used functions.  

if __name__ == "__main__":
    paragraph = input("enter a  paragraph: ")
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)
