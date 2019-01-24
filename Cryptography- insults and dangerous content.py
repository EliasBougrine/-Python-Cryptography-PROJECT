import numpy as np
import csv
import time





## Start a counter


start = time.time()





## Creation of a new file


# Create a new file where we will save the changed message
new_file = open('//Users/eliasbougrine/Desktop/project/Cryptographie/NewMessage.txt','w')





## Dangerous content


# Open the file containing the dangerous content
dangerous_content_file = open('//Users/eliasbougrine/Desktop/project/Cryptographie/Dangerous.csv')


# Read the file containing the dangerous content
read_dangerous_content = csv.reader(dangerous_content_file, delimiter = ',')


# Create a list containing the dangerous content
Dangerous_content_list = list(read_dangerous_content)[0]





## Insult content


# Open the file containing the insults
insult_file = open('//Users/eliasbougrine/Desktop/project/Cryptographie/Insult.csv')


# Read the file containing the insults
read_insults = csv.reader(insult_file, delimiter = ',')


# Create a list containing the insults
Insult_list = list(read_insults)[0]





## Open a message


# We have the following examples
    # explicite1
    # explicite2
    # explicite3


# Open the txt file
txt_file = open('//Users/eliasbougrine/Desktop/project/Cryptographie/explicite2.txt')


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





## Look for dangerous content


# Look if the txt file contains dangerous content
Dangerous_content = []
for i in range(0,w2):
    if Words2[i] in Dangerous_content_list:
        Dangerous_content.append(Words2[i])
dc = len(Dangerous_content)
if dc != 0 :
    print('The txt file contains a potential extreme content. Here are the words potentially dangerous:',Dangerous_content)
else: 
    print('The txt file does not contain a potential extreme content from the dictionnary.')





## Look for insults and replace them


# Look if the file contains insults
Insult = []
for i in range(0,w2):
    if Words2[i] in Insult_list:
        Insult.append(Words2[i])
ins = len(Insult)
if ins != 0:
    print('The txt file contains an insult:',Insult)
    print('We will remove this insult')
else:
    print('The txt file does not contain insult')


# Replace the insult
for i in range(0,ins):
    txt_read = txt_read.replace(Insult[i],'*****')





## Save the changes
    

# Save the changed message in the new file
new_file.write(txt_read)





## End the counter


end = time.time()
print('The computation time is:',end-start)