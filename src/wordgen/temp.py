import requests
from bs4 import BeautifulSoup

url  = 'http://elearning.ling.sinica.edu.tw/Cfindranking.php'
lim  = 93827
step = 300
for i in range(1, lim, step):
    start = i
    end   = start + step - 1
    if end >= lim:
        end = lim - 1
    print('start running from', start, 'to', end)
    r    = requests.post(url, data={'From': start, 'To': end})
    soup = BeautifulSoup(r.text.decode())
    for row in soup.findAll('table tr')[1:]:
        print(row.findAll('td'))
