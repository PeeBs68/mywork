# valueerror.py
# Using a normal input statement like the one below will just crash out to the terminal if the inoyt is in the wrong format
# Using a loop with ValueError will stay in the code and ask for a retry

while True:
  try:
    num1 = int(input("\nInput the first number in cents: "))
  except ValueError:
    print('Error - Your number must be an integer!')
    continue
  break

print (num1)

# above section replaces this simplier line whcih has no validations
# num1 = int(input("Input the first number in cents: "))

#References
#Details on how to handle non integer inputs taken from Stackoverflow
#https://stackoverflow.com/questions/62768087/how-can-i-not-allow-letters-and-only-allow-numbers-in-an-input-on-python-3 
#and details on the use of Try/Except taken from  
#https://www.w3schools.com/python/python_try_except.asp