import jinja2
import os
import random
import sys
from glob import glob
from slidegen import DataProvider
from slidegen import Generator
from wordgen import Wordgen

class WordgenProvider(DataProvider):
    def __init__(self):
        self.wg = Wordgen()

    def text(self):
        return self.wg.moistPhrase()

class GeneratorBridge(object):
    def __init__(self, generator):
        self.generator = generator

    def __hook(self, content):
        if random.randint(0, 3) > 0:
            slides.append('<section data-markdown>%s</section>\n' % content)
        else:
            slides.append('<section data-markdown data-background-iframe="%s" style="text-align: right;">\n%s\n</section>\n' % (random.choice(charts), content))

    def __getattr__(self, name):
        f = getattr(self.generator, name)
        def _proc(*args):
            return self.__hook(f(*args))
        return _proc

slides = []
charts = glob('public/Chart.js/samples/*')
charts = [ '/'.join(i.split('/')[1:]) for i in charts ]
g = GeneratorBridge(Generator(WordgenProvider()))

g.cover()
for i in range(18):
    if random.randint(0, 100) < 83:
        g.content()
    else:
        g.full_image()

os.chdir('public')
env = jinja2.environment.Environment()
env.loader = jinja2.FileSystemLoader('.')
template = env.get_template('template.html')
rendered = template.render(slides=slides)

with open('index.html', 'w', encoding='utf-8') as fo:
    fo.write(rendered)
