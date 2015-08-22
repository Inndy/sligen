from .crawler import Crawler
from .tools import *

class techorange(Crawler):
    def __init__(self):
        self.url = 'http://buzzorange.com/techorange/'
        self.queue = []
        self.r = requests.Session()

    def next(self):
        if not self.queue:
            self.grab()
        get_page(self,)

    def parse_page(self, doc):
        pass

    def get_page(self, url=None):
        if url == None:
            url = self.queue.pop()
        res = self.r.get(url)
        doc = bs4.BeautifulSoup(res.content)
        tree = doc.select('section .entry-box')
        def strip_tags(doc, selectors):
            for sel in selectors:
                for elem in doc.select(sel):
                    elem.decompose()
        strip_tags(tree, [ 'header', 'script' ])
        return tree

    def grab(self):
        res = self.r.get(self.url)
        self.doc = doc = bs4.BeautifulSoup(res.content)
        links = doc.select('article .entry-body header h2 a')
        queue = [ (l['href'], l.text) for l in links ]
        return queue

if __name__ == '__main__':
    c = techorange()
    c.next()
