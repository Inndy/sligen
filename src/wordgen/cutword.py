import math
import jieba
import jieba.posseg as pseg

jieba.set_dictionary('dict.txt.big')

qq  = ['物聯網']
ban = ['\n', ' ']

for word in qq:
	jieba.suggest_freq(word, True)

class Wordcount:
	def __init__(self):
		self.asset = []
		self.count = 0
		self.index = dict()
		self.flag  = 1
		self.tot_freq  = dict()
		self.tot_count = 0

	def totalFreq(self):
		if self.flag:
			print('start loading corpus frequency')
			f = open('tot_count.txt', 'r')
			for line in f.readlines():
				dat   = line.split('\t')
				word  = dat[0]
				count = int(dat[1])
				if word not in self.tot_freq:
					self.tot_freq[word] = count
					self.tot_count += count
			print('end loading corpus frequency')
			self.flag = 0

	def get_count(self):
		self.count = 0
		for row in self.asset:
			self.count += row[2]

	def get_diff(self, i):
		row   = self.asset[i]
		word  = row[0]
		count = row[2]
		if word not in self.tot_freq:
			self.tot_freq[word] = 0
		res = count / self.count - self.tot_freq[word] / self.tot_count
		return res

	def addText(self, text):
		for word, flag in pseg.cut(text):
			if word in self.index.keys():
				self.asset[self.index[word]][2] += 1
			else:
				self.index[word] = len(self.asset)
				self.asset.append([word, flag, 1])
		self.get_count()

	def deletecount(self, word):
		self.count -= self.asset[ self.index[word] ][2]
		self.asset[ self.index[word] ][2] = -10000000

	def preprocess(self):
		for row in self.asset:
			if len(row[0]) <= 1:
				self.deletecount(row[0])
		for word in ban:
			self.deletecount(row[0])
		bb = open('ban.txt', 'r')
		for line in bb.readlines():
			self.deletecount(row[0])
		for row in self.asset:
			t_flag = 1
			if any(row[1] in x for x in ['x', 'v', 'ns', 'n']):
				t_flag = 0
			if t_flag:
				self.deletecount(row[0])

	def showBuzzWord(self):
		self.totalFreq()
		self.preprocess()
		rate         = 5
		size         = len(self.asset)
		index_list   = [x for x in range(size)]
		sorted_index = sorted(index_list, key=lambda i: self.get_diff(i), reverse=True)
		return [self.asset[i] for i in sorted_index[:math.ceil(size * rate / 100)]]