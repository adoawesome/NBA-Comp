import requests
import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup

#Using this script to get all of the data from nba players


# Takes The player name, allowing for dynamic searching
playername= "doncic"

#Finds the basketball reference site for the player by google searching it
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
query = playername +"basketball-reference"
  
for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
    playerbbrefsite=j

#Prints the url of the bbref site of the player
print(playerbbrefsite)

page_response = requests.get(playerbbrefsite, timeout=10)
page_content = BeautifulSoup(page_response.text, "html.parser")

textcontent=""

for i in range(0, 20):
    paragraphs = page_content.find_all("p")[i].text
    textcontent=textcontent+paragraphs

print (textcontent)

tempcontent=textcontent.partition("lb (")
tempcontent=tempcontent[0]
print (tempcontent)
height=tempcontent[-9:-5]
weight=tempcontent[-3:]
print(height)
print(weight)
#tempcontent=tempcontent[2]
#tempcontent=tempcontent.partition(") Team")


#height=tempcontent[1]


try:
    ftheight=int(height[0])
except:
    ftheight=int(height[1])

if height[2]== "-":
    inheight=int(height[3])
else:
    inheight=int(height[2:4])
    
#except:
#    inheight=int(height[2])
    
#print(height[2:4])
#inheight=int(height[2])
totalheight=ftheight*12+inheight
print(height)
print(weight)

print (playername,"is",ftheight,"feet",inheight,"inches, for a total of",totalheight,"inches.")
print (playername,"weighs",weight,"pounds.")

