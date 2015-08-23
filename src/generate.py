import os
import sys
from slidegen import Generator
from slidegen import DataProvider

if len(sys.argv) < 2:
    print('Usage: %s output-path' % sys.argv[0])
    exit(1)

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

g = Generator(DataProvider())
g = GeneratorBridge(g, sys.argv[1])

g.cover()
g.content()
for i in range(4):
    g.content()
g.full_image()
