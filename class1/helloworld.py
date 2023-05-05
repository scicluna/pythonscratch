name = input("What's your name?").strip().title() #Ask user for name and strip whitespace and capitalize the first letter of each word
print(f'hello, {name}') #Calls the function with the user input as name [f" " is a template literal with variables in {}]

print('hello,', end=' ') #Can actually edit the end option directly (we only know this via the python docs)
print('World') #now they print on the same line, cool right? since the default for print ends with \n


