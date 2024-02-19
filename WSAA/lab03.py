import requests
import json

#Testing response
'''url = "http://google.com"

response = requests.get(url)
print(response) #200 is good!
'''

# Pull in Books from andreqbeatty1.pythonaanuywhere.com
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getbooks():
    response = requests.get(url)
    print(response)
    return response.json()

def findbooks(bookid):
    geturl = url + "/" + str(bookid)
    response = requests.get(geturl)
    print(response)
    return response.json()

def createbooks(book):
    response = requests.post(url, json=book)
    print(response)
    return response.json()

def updatebooks(bookid,bookupdate):
    puturl = url + "/" + str(bookid)
    response = requests.put(puturl, json=book)
    print(response)
    return response.json()

def deletebooks(bookid):
    deleteurl = url + "/" + str(bookid)
    response = requests.delete(deleteurl)
    print(response)
    return response.json()

if __name__ == "__main__":
    book= {
        'Author' : 'PB',
        'Title' : 'Very Fast and Very Furious VII',
        'Price' : 3100
    }
    bookupdate= {
        'Price' : 150
    }
    #print(getbooks())
    #print(findbooks(525))
    #print(createbooks(book))
    #print(updatebooks(525, bookupdate))
    #print(deletebooks(525))
