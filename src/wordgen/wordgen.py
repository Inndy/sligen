import random, itertools

class Wordgen(object):
    def __init__(self):
        self.verb  = []
        self.other = []
        f = open('data/newbuzzword.txt', 'r')
        for line in f.readlines():
            dat   = line.split('\t')
            word  = dat[0]
            part  = dat[1]
            if part[:-1] is 'v':
                self.verb.append(word)
            else:
                self.other.append(word)

    def moistPhrase(self):
        XD = 6
        res = [self.other[i] for i in random.sample(range(len(self.other)), 2)]
        if random.randint(0, XD) == 0:
            verb_len = len(self.verb)
            res = [self.verb[random.randint(0, verb_len - 1)]] + res
        return ''.join(res)