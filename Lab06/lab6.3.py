# Lab06.3
# Create the menu items function

def doAdd():
    print("Adding")

def doView():
    print("Viewing")

def menu():
    print("Here are your options")
    print("\t(a) Add new student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    item = (input("Type one letter (a/v/q):  "))

    return item

item = menu()
while (item != "q"):
    if item == "a":
        doAdd()
    elif item == "v":
        doView()
    elif item != "q":
        print ("It needs to be either a,v,q")
    item = menu()
print (f"You choose: {item} to quit")
