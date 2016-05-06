import bs4
import requests

response = requests.get('http://search.itooza.com/index.htm#indexTable2')
response.encoding='cp949'
data = bs4.BeautifulSoup(response.text, 'lxml')

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
table_body = data.tbody

rows = table_body.find_all('tr')

for row in rows:
	if (row.th.string == '주당 배당금'):
		print(row.th)