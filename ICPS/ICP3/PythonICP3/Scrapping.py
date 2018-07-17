import urllib.request
from bs4 import BeautifulSoup
import os

# Assigning link to a variable

myLink = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# Opens the URL
getLink=urllib.request.urlopen(myLink)

# Converts to HTML
soup = BeautifulSoup(getLink,  "html.parser")
# Prints Header for the wiki page
print(soup.h1.text)
for link in soup.findAll('a'):
    # Prints links with href in anchor tags
    print(link.get('href'))

    # Goes to the table and collects data from the class  wikitable sortable plainrowheaders
table = soup.find("table", { "class" : "wikitable sortable plainrowheaders" })

# looping all elements in tr tags
for row in table.findAll('tr'):
    for r in row.findAll('td'):
        cells = r.text
        # prints td elements
        print(cells)
        elements = row.find('th')
        # prints th elements
        print(elements.text)



