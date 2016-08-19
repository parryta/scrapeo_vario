import json
import requests

url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)%0A%09%09&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json"

req = requests.get(url)

if req.status_code == 200:

    decoded = json.loads(req.text)

    for element in decoded["query"]["results"]["quote"]:
        print(element["symbol"]+" "+element["EarningsShare"])
