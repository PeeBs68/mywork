# Script to read in a string - strips and leading or trailing spaces and convert it to lower case
# Output the length of the input and output strings and indicate the spaces saved

string1 = input("Enter a string with leading and training spaces: ")

# Remove white space at start and end
#string2 = string1.strip()
# convert all to lower case
#string3 = string2.lower()

# strin() and lower() can be combined like this
string3 = string1.strip().lower()

# Number of spaces saved (len1 - len2)
num2 = (len(string1)-len(string3))

print(f"The Original string is : '{string1}' \nAnd the normalised string is '{string3}' \nWe saved {num2} spaces")

