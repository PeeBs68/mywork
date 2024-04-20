from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')


'''
@app.route('/')
def index():
    return("Hello there")

@app.route('/books', methods = ['GET'])
def getall():
    return("Get all")

@app.route('/books/<int:id>', methods = ['GET'])
def findbyid(id):
    return(f"Find by ID {id}")

@app.route('/books', methods = ['POST'])
def create():
    # read JSON...need to test this using POSTMAN so as to add the details in JSON format
    jsonstring = request.json

    return(f"Create {jsonstring}")

@app.route('/books/<int:id>', methods = ['PUT'])
def update(id):
    # read JSON...need to test this using POSTMAN so as to add the details in JSON format
    jsonstring = request.json

    return(f"Update {id} {jsonstring}")

@app.route('/books/<int:id>', methods = ['DELETE'])
def delete(id):
    return(f"Delete by ID {id}")
'''
if __name__ == "__main__":
    app.run(debug=True)

