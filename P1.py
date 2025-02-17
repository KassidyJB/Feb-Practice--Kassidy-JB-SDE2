#1. Ask user input
#2. Loop through characters (For Loop)
#3. Get 1st letter of each word (Indexing)
#4. Convert to uppercase (.upper())
#5. Return acronym

word = input(f"Enter a sentence or phrase >\n")#.replace()

#def acro(word):
    #for i in range(len(word)):
        #str.captialize(word)
        
            
    #return word

def acro(word):
    for i in range(word): #Looping through letters in the word
        word.split() #if input is a phrase, split based on spaces 
        #so spaces don't give a problem and work in favor
        new_word = print(word[0]).upper() #print the first letter of word by
        # 0 (first index) and capitalize it
    return new_word.join()#Join all first letters together
