import requests
from bs4 import BeautifulSoup

term = input("Enter the requested definition : ")
r = requests.get("https://www.urbandictionary.com/define.php?term="+term)
soup = BeautifulSoup(r.text,'html.parser')
content = soup.find("div", id="content")

title = content.find("a",class_="word").text
print("\n"+title)
definitiontext = content.find("div",class_="meaning").text
print("\n"+definitiontext)
examplee = content.find("div",class_="example").text
source = content.find("div",class_="contributor").text

print("\n"+"Example: "+examplee)
print("\n"+source+ " @ www.urbandictionary.com")