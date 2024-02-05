import requests
import csv

from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

retrieveTags = ['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage', 'Direction']

#print (doc.toprettyxml())

# save to xml if needed
# with open("trainxml.xml","w") as xmlfp:
#    doc.writexml(xmlfp)

with open("latitudes.csv", mode = "w", newline = '') as train_file:
# left out , delimeter = '\t' as it was causing an error
    train_writer = csv.writer(train_file, quotechar = '"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
    # To just get the TrainCode    
    #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    #traincode = traincodenode.firstChild.nodeValue.strip()
    #print(traincode)
    # To just get the TrainLatitidude   
        #trainlatitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
        #latitude = trainlatitudenode.firstChild.nodeValue.strip()
    #print(latitude)
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            print("Hi")
            print(datanode)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)


