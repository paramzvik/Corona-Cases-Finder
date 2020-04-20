import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
req = requests.get(url)

wrap = BeautifulSoup(req.text,"html.parser")
data = wrap.find_all("div",class_="maincounter-number")

print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())