# Lab06.2
# Create the menu items function

def menu():
    print("Here are your options")
    print("\t(a) Add new student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    item = (input("Type one letter (a/v/q):  "))

    return item

item = menu()
print (f"You choose: {item}")
