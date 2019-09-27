import requests
import json

# Where is International Space Station now?
response = requests.get("http://api.open-notify.org/iss-now.json")
# response = requests.put("URL", data={'k':'value'})
print(response.status_code)
print(response.content)

# What's the response for non-existing resource?
response = requests.get("http://api.open-notify.org/iss-pass.json")
print(response.status_code)



# Set up the parameters we want to pass to the API.
# The latitude and longitude of
# parameters = {"lat": 40.71, "lon": -74}       # New York City
parameters = {"lat": 19.0760, "lon": 72.8777}   # Mumbai

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)


data = response.json()  # Convert to JSON string
print(type(data))       # its a dictionary
print(data)

# # This gets the same data as the command above
# response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# print(response.content)



parameters = {"segmentLink": 17, "instrument": "OPTIDX", "symbol": "NIFTY", "date": "26SEP2019"}
URL = "https://nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp"
response = requests.get(URL, params=parameters)
#print(response.headers)
print(response.content)
print(response.json())      # output is html not json 


url = 'https://www.jpmorganchase.com/corporate/About-JPMC/about-us.htm'
contents = requests.get(url)
contents.status_code
contents.text

from bs4 import BeautifulSoup

page = BeautifulSoup(contents.text, 'html.parser')

print(page.prettify())
page.find_all(id='copyright')
page.find_all(class_='about')
page.find_all('img')


