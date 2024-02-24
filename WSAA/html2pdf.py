import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://en.wikipedia.org"
#targetUrl = "https://www.atu.ie/"

apikey = cfg["html2pdfkey"]
#apikey = "Tsxnu5BVqAtLeB9DI6FPbeKSjwFeUqEWIRS7IlPMT04d96RrkVfuDUS7O0nPvavd"
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'html': targetUrl,'apiKey': apikey}
parsedparams = urllib.parse.urlencode(params)

requesturl = apiurl +"?" + parsedparams 
print (requesturl)

response = requests.get(requesturl)
print(response.status_code)

result = response.content
with open ("document.pdf", "wb") as handler:
    handler.write(result)



