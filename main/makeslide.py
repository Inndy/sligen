import jinja2
from jinja2.environment import Environment
import glob
import random

env = Environment()
env.loader = jinja2.FileSystemLoader('.')
tem = env.get_template('./temp.html')
s_all = []

cht = []
for s in glob.glob('Chart.js/samples/*'):
    print(s)
    cht.append(s)

for f in glob.glob('slides/*.md'):
    print(f)
    with open(f) as fo:
        i = random.randint(0,3)
        if i > 2:
            s_all.append('<section data-markdown>\n'+fo.read()+'\n</section>\n')
        else:
            r = random.choice(cht)
            s_all.append('<section data-markdown data-background-iframe="'+r+'" style="text-align: right;">\n'+fo.read()+'\n</section>\n')

out = tem.render(slides = s_all)

index = open("output.html", "w")
index.write(out)
