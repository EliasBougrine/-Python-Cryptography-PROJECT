import numpy as np
import csv
import time





## Start a counter


start = time.time()





## Dictionnary


# Open the dico
txt_dico = open('//Users/eliasbougrine/Desktop/project/Cryptographie/dico.txt')


# Read the txt dico
txt_read_dico = txt_dico.read()
td = len(txt_read_dico)


# Remove the '\n' at the end of the words
txt_read_dico2 = txt_read_dico.replace('\n',' ')


# Create a list with the different words of the txt dico
dico = []
Position_of_the_spaces = [-1]
# Find the positions of the different spaces in the txt dico
for i in range(0,td):
    if txt_read_dico2[i] == ' ':
        Position_of_the_spaces.append(i)
    p = len(Position_of_the_spaces)
# Take back the different words of the txt dico
for k in range(0,p-1):
    word = txt_read_dico2[Position_of_the_spaces[k]+1:Position_of_the_spaces[k+1]]
    # Put the word in low letters
    word = word.lower()
    dico.append(word)
# Take back the last word of the txt dico
word = txt_read_dico2[Position_of_the_spaces[p-1]+1:td]
# Put the last word in slower letter
word = word.lower()
dico.append(word)





## Txt crypted message


# We have different examples:
    # Caesar1
    # Caesar2
    # Caesar3
    # Vigenere1
    # Vigenere2
    # Vigenere3


# Open the txt file
txt_file = open('//Users/eliasbougrine/Desktop/project/Cryptographie/Vigenere3.txt')


# Read the txt file
txt_read = txt_file.read()
t = len(txt_read)


# Remove the '\n' at the end of the words
txt_read2 = txt_read.replace('\n',' ')


# Create a list with the different words of the txt file
Words = []
Position_of_the_spaces = [-1]
# Find the positions of the different spaces in the txt file
for i in range(0,t):
    if txt_read2[i] == ' ':
        Position_of_the_spaces.append(i)
    p = len(Position_of_the_spaces)
# Take back the different words of the txt file
for k in range(0,p-1):
    word = txt_read2[Position_of_the_spaces[k]+1:Position_of_the_spaces[k+1]]
    # Put the word in low letters
    word = word.lower()
    Words.append(word)
# Take back the last word of the txt file
word = txt_read2[Position_of_the_spaces[p-1]+1:t]
# Put the last word in slower letter
word = word.lower()
Words.append(word)
w = len(Words)


# Remove the special characters
Words2 = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"'"]
# Test each word of the txt file
for i in range(0,w):
    word = Words[i]
    wo = len(word)
    # We create a list of the position of the special characters of each word
    Position_of_the_special_char = []
    for j in range(0,wo):
        if word[j] not in alphabet:
            Position_of_the_special_char.append(j)
    psc = len(Position_of_the_special_char)
    # We finally remove the special characters
    a = 0
    while psc != 0 :
        word = word.replace(word[Position_of_the_special_char[a]],'')
        psc = psc - 1
        a = a + 1
    Words2.append(word)
w2 = len(Words2)





## Cesar Method


# Test if the message has been crypted with the Cesar method and determine the key
alphab = "abcdefghijklmnopqrstuvwxyz"
# We do the test for the 25 possible keys
for i in range(1,26):
    Words3 = []
    for j in range(0,w2):
        new_word = ''
        word = Words2[j]
        wo = len(word)
        for k in range(0,wo):
            # Find the position of each letter on the alphab list
            n = alphab.find(word[k])
            # Add to the position the supposed encryption key
            n = n + i
            # Be sure that n is inferior of the len of the alphab
            if n > len(alphab)-1:
                n = n - len(alphab)
            # Do the decryption
            new_word = new_word + alphab[n]
        Words3.append(new_word)
    w3 = len(Words3)
    # Test if the new words are in the dico
    c = 0   # Counter to know how many words of the list are in the dico
    for m in range(0,w3):
        word = Words3[m]
        if word in dico:
            c = c+1
    # Calculate the percentage of words that are in the dico
    perc = float(c)/w3
    # If more than 90% of the words of the list are in the dico, this is the good key
    if perc > 0.9:
        key = i
        break
perc2 = 0
if perc > 0.9:
    w3 = len(Words3)
    print('This message has been crypted with the Caesar method. Here is the key:',key)
    print('The message is:',Words3)





## Vigenere Method


# Else, test if the message has been crypted with the Vigenere method
else:
    # We generate all the possible keys with 3-letters keys limit
    keys_list = []
    possible_key = ''
    for i in range(0,26):
        for j in range(0,26):
            possible_key = alphab[i] + alphab[j]
            keys_list.append(possible_key)
            for k in range(0,26):
                possible_key = alphab[i] + alphab[j] + alphab[k]
                keys_list.append(possible_key)
    kl = len(keys_list)
    # Test the Vigenere method for each key
    for i in range(0,kl):
        potential_key = keys_list[i]
        Words3 = []
        # We retrieve each word
        for j in range(0,w2):
            new_word = ''
            word = Words2[j]
            wo = len(word)
            for k in range(0,wo):
                # Find the position of the letter of the word in the alphabet list
                n = alphab.find(word[k])
                # If the potential key is smaller than the word
                poscle = k%len(potential_key)
                # Find the corresponding letter
                alpha = potential_key[poscle]
                # Retrieve the position of alpha to decrypt
                d = (n - alphab.find(alpha))%26
                new_word = new_word + alphab[d]
            Words3.append(new_word)
        w3 = len(Words3)
        # Test if the new words are in the dico
        c = 0   # Count how many words of the list are in the dico
        for p in range(0,w3):
            word = Words3[p]
            if word in dico:
                c = c+1
        # Calculate the percentage of words that are in the dico
        perc2 = float(c)/w3
        # If more than 90% of the words of the list are in the dico, this is the good key
        if perc2 > 0.9:
            key = potential_key
            break

if perc2 > 0.9:
    print('This message has been crypted with the Vigenere method. Here is the key:',key)
    print('The message is:',Words3)





## Dangerous content


# Open the file containing the dangerous content
dangerous_content_file = open('//Users/eliasbougrine/Desktop/project/Cryptographie/Dangerous.csv')


# Read the file containing the dangerous content
read_dangerous_content = csv.reader(dangerous_content_file, delimiter = ',')


# Create a list containing the dangerous content
Dangerous_content_list = list(read_dangerous_content)[0]


# Look if the message contains dangerous content
Dangerous_content = []
for i in range(0,w3):
    if Words3[i] in Dangerous_content_list:
        Dangerous_content.append(Words3[i])
dc = len(Dangerous_content)
if dc != 0 :
    print('The txt file contains a potential extreme content. Here are the words potentially dangerous:',Dangerous_content)
else: 
    print('The txt file does not contain a potential extreme content from the dictionnary.')





## End the counter


end = time.time()
print('The computation time is:',end-start)