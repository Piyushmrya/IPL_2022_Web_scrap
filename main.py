# Step 0 : import/install all the reqirements 
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

# Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 : Parse the HTML / creating the Soup
soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())


# Step 3 :  HTML Tree traversal
# 
#  Commonly used types of objects:
# 1. Tag                           print(type(title)) 
# 2. NavigableString               print(type(title.string ))
# 3. BeautifulSoup                 print(type(soup))
# 4. Comment

# Get the title of the HTML page
title = soup.title

#  Get all the paragraph from the page
paras = soup.find_all('p')
# print(paras)

#  Get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)

# print(soup.find('p'))                  Gives first Element in the HTML page
# print(soup.find('p')['class'])         Gets classes of any element in the HTML page
# print(soup.find_all('p',class_='lead'))   Gives all the elements with class = lead
# print(soup.find('p').get_text())
# print(soup.get_text())                    Gives all the text of the page

# # Get all the links on the page 
# for link in anchors:
#     print(link.get('href'))

# Problem : 1) REPEATED LINKS , 2) CANT GO TO THE LINK BY CLICKING
# Solution :
all_links = set()
for link in anchors:
    if (link.get('href') != '#'):
        links = "https://codewithharry.com"+link.get('href')
        all_links.add(link)
        # print(links)


# Lets see the Last one #Comment

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup,features="html5lib")                  #Converted markup to a soup
# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))

nav_content = soup.find(id='nav-content')
# # print(nav_content.contents)
# for elem in nav_content.children:
#     print(elem)

## .contents :  A tag's children are available as a list
## .children : A tag's children are availabe as a generator                 #works faster
# for item in nav_content.strings:
#     print(item)

# for item in nav_content.stripped_strings:
#     print(item)

# print(nav_content.parent)
# print(nav_content.parents)             # getting a generator , which means we can iterate over it so lessgoo
for item in nav_content.parents:
    print(item.prettify())
