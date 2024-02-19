import requests
import json
from lab03 import getbooks

#print(getbooks())

all_books = getbooks()
#print (all_books)
count = 0
price = 0

for book in all_books:
    price += book["Price"]
    count += 1


print("Average price of books is : ", price/count)