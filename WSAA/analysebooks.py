from bookapidao import getallbooks

books = getallbooks()
total = 0
count = 0

for book in books:
    total += book["Price"]
    count += 1
#print(count)
print ("Average Price of all books = ", total/count)
#print(books)