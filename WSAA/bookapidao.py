import requests
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getbookbyid(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def deletebook(id):
    geturl = url + "/" + str(id)
    response = requests.delete(geturl)
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
    return response.json()


def updatebook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()



if __name__ == "__main__":
    book= {
        'Author' : 'PB',
        'Title' : 'Very Fast and Very Furious II',
        'Price' : 300
    }
    bookdiff= {
        'Price' : 3000
    }
    #print(getallbooks())
    #print(getbookbyid(477))
    #print(deletebook(477))
    #print(createbook(book))
    #print(updatebook(497, bookdiff))




