from .crawler import Crawler
from .tools import *

try:
    from .config import pixbay as config
except ImportError:
    print('Please config src/crawlers/config.py')
    exit(1)

class pixabay(Crawler):
    def __init__(self):
        self.url = 'https://pixabay.com/en/photos/?orientation=&image_type=&cat=science&colors=&q=&order=best&pagi=%d'
        self.index = 1
        self.queue = []
        self.r = requests.Session()
        self.login(config['user'], config['pass'])

    def next(self):
        if not self.queue:
            self.grab()
        url = self.get_download_link(self.queue.pop())
        return lambda: self.r.get(url).content

    def login(self, usr, pwd):
        data = {
            'username': usr,
            'password': pwd
        }
        self.r.post('https://pixabay.com/en/accounts/login/?next=/en/accounts/logout/', data=data)

    def get_download_link(self, url):
        res = self.r.get(url)
        doc = bs4.BeautifulSoup(res.content)
        imgurl = doc.select('input[name=download]')[1]['value']
        return 'https://pixabay.com/en/photos/download/%s?attachment' % imgurl

    def parse_page(self, doc):
        photos = doc.select('#photo_grid .item a')
        return ( 'https://pixabay.com' + i['href'] for i in photos )

    def get_page(self, url=None):
        res = self.r.get(url)
        doc = bs4.BeautifulSoup(res.content)
        return self.parse_page(doc)

    def grab(self):
        page = self.get_page(self.url % self.index)
        self.index += 1
        self.queue += list(page)
