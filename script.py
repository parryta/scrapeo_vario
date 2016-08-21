import json
import requests
import datetime

url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22BBVA%22%2C%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)%0A%09%09&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json"

req = requests.get(url)
print("--->", requests.head(url))

outputFile = open('salidas_a_txt.txt', 'a')

outputFile.write('Welcome to my new file \n')

if req.status_code == 200:

    decoded = json.loads(req.text)
    outputFile.write("TimeStamp ---> \t" + str(datetime.datetime.now()) + "\n -------- \n")
    print ("TimeStamp: \n" + format(str(datetime.datetime.now())) + "\n --------")

    for element in decoded["query"]["results"]["quote"]:
        print(element["symbol"] + " " + element["Ask"])
        outputFile.write(element["symbol"] + " " + element["Ask"]+"\n")

outputFile.close()
