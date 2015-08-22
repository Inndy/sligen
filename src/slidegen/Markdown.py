class MarkdownDocument(object):
    def __init__(self):
        self.container = []

    def add(self, obj):
        if type(obj) is list:
            self.container += obj
        else:
            self.container.append(obj)

    def render(self):
        return ''.join(str(i) for i in self.container)

    def __str__(self):
        return self.render()

class MarkdownObject(object):
    def __init__(self):
        pass

    def __str__(self):
        return self.render()

class Heading(MarkdownObject):
    def __init__(self, text, level=1):
        self.level = level
        self.text = text

    def render(self):
        prefix = '#' * min(6, self.level)
        return '%s %s\n\n' % (prefix, self.text)

class Paragraph(MarkdownObject):
    def __init__(self, text):
        self.text = text

    def render(self):
        return '%s\n\n' % self.text

class FencedText(MarkdownObject):
    def __init__(self, text):
        self.text = text

    def render(self):
        return '```\n%s\n```\n' % self.text

class QuotedText(MarkdownObject):
    def __init__(self, text):
        self.text = text

    def render(self):
        return '%s\n' % ''.join('> %s\n' % line for line in self.text.split('\n'))

class ItemList(MarkdownObject):
    def __init__(self, items=[]):
        self.items = list(items)

    def add(self, obj):
        if type(obj) is list:
            self.items += obj
        else:
            self.items.append(obj)

    def render(self):
        return '%s\n' % '\n'.join('- %s' % item for item in self.items)

class Seperator(MarkdownObject):
    def __init__(self):
        pass

    def render(self):
        return '---\n\n'

if __name__ == '__main__':
    doc = MarkdownDocument()
    doc.add(Heading('SlideGen Project'))
    doc.add(Paragraph('Make you pitching like a boss'))
    doc.add(Heading('What is this?', 2))
    doc.add(QuotedText('such hackathon,\nso food,\nwow pitch.'))
    doc.add(Heading('How to hackathon?', 2))
    items = ItemList()
    items.add('Food')
    items.add('Talk')
    items.add('Prize')
    items.add('Slides')
    doc.add(items)
    print(doc.render())

