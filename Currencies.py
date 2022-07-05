import requests
import xmltodict

url = "http://www.cbr.ru/scripts/XML_val.asp"
response = requests.get(url)

response.content

data = xmltodict.parse(response.content)

items = []
for item in data['Valuta']['Item']:
    items.append(item)

my_array = []
for item in data['Valuta']['Item']:
    my_set = [item['Name'], item['EngName'], item['Nominal'], item['ParentCode']];
    my_array.append(my_set)
    print(my_set)
