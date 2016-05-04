import bs4
import requests

data = requests.get('http://search.itooza.com/index.htm#indexTable2')
data.encoding='cp949'
data = bs4.BeautifulSoup(data.text)
print(data)