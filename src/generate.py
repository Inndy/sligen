import os
import sys
import random
from slidegen import Generator
from slidegen import DataProvider
from wordgen import Wordgen

if len(sys.argv) < 2:
    print('Usage: %s output-path' % sys.argv[0])
    exit(1)

class WordgenProvider(DataProvider):
    def __init__(self):
        self.wg = Wordgen()

    def text(self):
        return self.wg.moistPhrase()

class GeneratorBridge(object):
    def __init__(self, generator, output_path):
        self.generator = generator
        self.path = output_path
        self.index = 0

    def __hook(self, val):
        self.index += 1
        with open(os.path.join(self.path, '%.3d.md' % self.index), 'w') as fo:
            fo.write(val)
        return val

    def __getattr__(self, name):
        f = getattr(self.generator, name)
        def _proc(*args):
            return self.__hook(f(*args))
        return _proc

g = Generator(WordgenProvider())
g = GeneratorBridge(g, sys.argv[1])

g.cover()
for i in range(18):
    if random.randint(0, 100) < 77:
        g.content()
    else:
        g.full_image()
