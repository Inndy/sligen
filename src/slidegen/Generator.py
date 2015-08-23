import random
from .Markdown import *

class Generator(object):
    def __init__(self, data_providor):
        self.dp = data_providor

    def cover(self):
        doc = MarkdownDocument()
        doc.add(Heading(self.dp.topic()))
        doc.add(Heading(self.dp.title(), 2))
        doc.add(Seperator())
        return doc.render()

    def full_image(self):
        doc = MarkdownDocument()
        doc.add('<div class="fullimg">\n')
        doc.add(Image(self.dp.image('big')))
        doc.add('</div>\n')
        doc.add(Seperator())
        return doc.render()

    def content(self):
        doc = MarkdownDocument()
        doc.add(Heading(self.dp.title(), 3))
        doc.add(ItemList([ self.dp.text() for _ in range(random.randint(3, 6)) ]))
        doc.add(Seperator())
        return doc.render()
