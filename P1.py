'''Write a program that takes a phrase or sentence as 
input (e.g., "Federal Bureau of Investigation")
and generates the corresponding acronym (e.g., "FBI").
The acronym should be formed by taking the first letter 
of each word and converting it to uppercase.'''

#Pseudo/think

'''
1. Ask user input
2. Loop through characters (For Loop)
3. Get 1st letter of each word (Indexing)
4. Convert to uppercase (.upper())
5. Return acronym'''

word = input(f"Enter a sentence or phrase >\n")

def acro(word):
    for i in word:
        

