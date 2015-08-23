import random, itertools

class Wordgen(object):
    def __init__(self):
        self.verb       = []
        self.final_noun = []
        self.other      = []
        f = open('data/newbuzzword.txt', 'r', encoding='utf-8')
        for line in f:
            dat   = line.split('\t')
            word  = dat[0]
            part  = dat[1][:-1]
            if part == 'v':
                self.verb.append(word)
            elif part == 'fn':
                self.final_noun.append(word)
            else:
                self.other.append(word)

    def moistPhrase(self):
        verb_prob       = 6
        final_noun_prob = 2
        verb_len = len(self.verb)
        final_noun_len = len(self.final_noun)
        res = []
        if random.randint(0, verb_prob) == 0:
            res += [ self.verb[random.randint(0, verb_len - 1)] ]
        res += [self.other[i] for i in random.sample(range(len(self.other)), 2)]
        if random.randint(0, final_noun_prob) == 0:
            res += [ self.final_noun[random.randint(0, final_noun_len - 1)] ]
        return ''.join(res)