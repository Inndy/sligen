import hashlib
import random
from datetime import datetime
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image

doge_flavors = [
    'wow', 'wow', 'wow', 'wowah', 'amaze', 'shibaaarrr', 'plz no',
]

doge_prefixes = [
    'so {}', 'much {}', 'many {}', 'very {}', 'such {}', 'how to {}?',
    'good {}', 'nice {}'
]

doge_colors = ['#f44336', '#e91e63', '#9c27b0', '#673ab7', '#3f51b5',
    '#2196f3', '#03a9f4', '#00bcd4', '#009688', '#4caf50', '#8bc34a',
    '#cddc39', '#ffeb3b', '#ffc107', '#ff9800', '#ff5722', '#795548']

def has_overlap(rect_a, rect_b):
    x1, y1, w1, h1 = rect_a
    x2, y2, w2, h2 = rect_b
    return not ((x1 + w1) < x2 or (x2 + w2) < x1 or (y1 + h1) < y2 or (y2 + h2) < y1)

def dogify(keywords):
    sentences = []
    for keyword in keywords:
        sentences.append(random.choice(doge_prefixes).format(keyword))
    sentences += (random.sample(doge_flavors, random.randint(3, 5)))
    return sentences

def generate(keywords, slug=None):
    sentences = dogify(keywords)
    with Drawing() as draw:
        draw.font = 'doge_project/assets/comic_sans.ttf'
        draw.text_antialias = True
        with Image(filename='doge_project/assets/doge.jpg') as source:
            with source.convert('png') as doge:
                scene = [(222, 75, 144, 144)]   # Doge face
                for sentence in sentences:
                    draw.fill_color = Color(random.choice(doge_colors))
                    for tries in range(10):
                        draw.font_size = random.randint(24, 48)
                        metrics = draw.get_font_metrics(doge, sentence)
                        x = random.randint(0, int(doge.width - metrics.text_width))
                        y = random.randint(0, int(doge.height - metrics.text_height))
                        rect = (x, y, int(metrics.text_width), int(metrics.text_height))
                        if not any(has_overlap(rect, i) for i in scene):
                            scene.append(rect)
                            break
                    draw.text(x, y, sentence)
                draw.draw(doge)
                timestamp = hashlib.sha1(datetime.now().isoformat(' ').encode()).hexdigest()
                if slug:
                    doge.save(filename=('files/{}.png'.format(slug)))
                else:
                    doge.save(filename=('files/{}.png'.format(timestamp)))
