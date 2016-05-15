import bs4
from urllib import parse
import requests

def get_dividend(company):     
#  company = input('Company(ex, 한국기업평가) : ')
  print()
  print('*** %s ***' % company)

  if ';' in company:
    company = company.replace(';', '')
    print('new : %s' % company)

  if not company:
    company = '한국기업평가'
  company_cp949 = parse.quote(company.encode('cp949'))


  url = 'http://search.itooza.com/index.htm?seName=' + company_cp949 + '&x=24&y=7#indexTable2'
  response = requests.get(url)
  response.encoding='cp949'
  data = bs4.BeautifulSoup(response.text, 'html.parser')

  '''
  <body>
    <div id='wrap'>
      <div id='container'>
        <div id='content'>
          <div id='indexTable'>
            <div id='indexTable2'>
            	<table border='1' class='ex'>
            	  <tbody>
            	    <tr>
            	      <th><abbr title='주당 배당금'>주당 배당금</abbr></th>
            	      <td>1,537</td>
            	      <td>1,682</td>
            	    </tr>
  </body>

  '''

  table = data.find('div', attrs={'id':'indexTable2'})
  if not table:
    return
  trs = table.find_all('tr')
  if not trs:
    return

  for tr in trs:
  	if tr.th.text == '주당 배당금':
  		print(tr.th.text)
  		tds = tr.find_all('td')
  		for td in tds:
  			print(td.text, end=' ')
  print()

url = 'http://paxnet.moneta.co.kr/stock/searchStock/searchStock.jsp?section=0'
response = requests.get(url)
response.encoding='cp949'
data = bs4.BeautifulSoup(response.text, 'html.parser')
trs = data.find_all('tr')
for tr in trs:
  tds = tr.find_all('a')
  for td in tds:
    get_dividend(td.text)
print()

