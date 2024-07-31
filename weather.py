import requests
import json
import csv
import pandas as pd 

city='kolhapur'
key="800e2b0d2f58aa5ce2d733616cf95411"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
response=requests.get(url)

data=response.json()
print(json.dumps(data, indent=4))

dict= json.loads(data)
df = json_normalize(dict["weather"]) 

# Example 2: Convert JSON to DataFrame Using read_json()
df2 = pd.read_json(jsonStr, orient ='index')

#dataFrame = pd.read_json(&quot;subject.json&quot;)
print(dataFrame)
