import requests
from bs4 import BeautifulSoup

url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

lst = soup.find_all('p')

def clean_item(my_item):
    position = my_item.find('</p')
    return my_item[3:position]

for item in lst[0:48]:
    print(clean_item(str(item)))
