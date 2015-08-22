class DataProvider(object):
    def __init__(self):
        raise NotImplementedError('Please ')

class FakeDataProvider(DataProvider):
    IMAGES = '''
        http://i.imgur.com/AzYR9Jg.gif
        http://i.imgur.com/Mfc3anw.gif
        http://i.imgur.com/rqcnmc1.gif
        http://i.imgur.com/I1K6Tr0.gif
        http://i.imgur.com/XAbExXi.gif
        http://i.imgur.com/ehB8CFG.gif
        http://i.imgur.com/uL4ROxF.gif
        http://i.imgur.com/MI8OE8L.gif
        http://i.imgur.com/7ZlanhU.gif
        http://i.imgur.com/sU6f1Ir.gif
    '''.split()

    def __init__(self):
        self.counter = 0

    def image(self, size='medium'):
        self.counter += 1
        return FakeDataProvider.IMAGES[self.counter]

if __name__ == '__main__':
    p = FakeDataProvider()
    print(p.image())
    print(p.image())
    print(p.image())
    print(p.image())
