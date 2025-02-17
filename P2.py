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

def select():
    if temp == "Celsius":
        print(C)
    elif temp == "Fahrenheit":
        print(F)
    elif temp == "Kelvin":
        print(K)
pass

def C():
    cel = input(f'''What temp scale would you 
    like to convert to? K/F? \n>''')
    if 

pass

def F():
    fah = input(f'''What temp scale would you 
    like to convert to? C/K? \n>''')
pass

def K():
    kel = input(f'''What temp scale would you 
    like to convert to? C/F? \n>''')