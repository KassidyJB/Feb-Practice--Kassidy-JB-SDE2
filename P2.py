'''
Create a program that first 
asks the user which temperature scale they would like to convert 
from (e.g., Celsius, Fahrenheit, Kelvin).
Then, ask which temperature scale they would like to convert to.
Afterward, prompt the user for the temperature value and
perform the conversion.
'''
#Pseudo/think
#1. Ask user what temp they want to convert FROM
#2. Ask what temp scale they want to convert TO
#3. Ask for temp value for so we can convert
#4. Convert (possibly need mathematics)
temp = input(f'''Which temperature scale 
would you like to convert from? 
Celcius? Fahrenheit? or Kelvin?\n>''')
#Creating a select function to control users input and what to 
#respond with accordingly
def select():
    if temp == "Celsius":
        print(C)
    elif temp == "Fahrenheit":
        print(F)
    elif temp == "Kelvin":
        print(K)
select()

#Converting celcius to kelvin or fahren based on input
def C():
    cel = input(f'''What temp scale would you 
    like to convert to? K/F? \n>''')
    if cel == "K":
        new_cel = {cel}+273.15
    elif cel == "F":
        new_cel = ({cel}*9/5) + 32

    return new_cel#returning the new variable and reassigning after
    #fully confverting

#Converting fahren to Kelvin or celcius based on input
def F():
    fah = input(f'''What temp scale would you 
    like to convert to? C/K? \n>''')
    if fah == "C":
        new_fah = ({fah} - 32)*5/9
    elif fah == "K":
        new_fah = ({fah} - 32)* 5/9 + 273.15 #setting & assigning all computations
        #to a new variable
    return new_fah




def K():
    kel = input(f'''What temp scale would you 
    like to convert to? C/F? \n>''')#based on user input in select function,
    #there'll be a more specific quesiton
    if kel == "C":
        new_kel = {kel} - 273.15 
    elif kel == "F":
        new_kel = ({kel} - 273.15)* 9/5 + 32
    return new_kel
