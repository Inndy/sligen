from glob import glob
import random

class DataProviderBase(object):
    def __init__(self):
        '''
        Init your data provider
        '''
        raise NotImplementedError('Please ')

    def image(self, size):
        '''
        size in ['big', 'medium', 'small']

        big for full page background
        medium for a foreground image
        small for half-page image
        '''
        raise NotImplementedError('Please ')

    def topic(self):
        '''
        generate a slide topic
        '''
        raise NotImplementedError('Please ')

    def title(self):
        '''
        generate a slide page title
        '''
        raise NotImplementedError('Please ')

    def text(self):
        '''
        generate an paragraph for slide content
        '''
        raise NotImplementedError('Please ')

class DataProvider(DataProviderBase):
    def __init__(self):
        self.counter = 0

    def image(self, size='medium'):
        return random.choice(glob('data/img/*'))

    def who(self):
        return random.choice([
            'Denny', 'RS', '開源社長', '大萌神', '畢總召', 'Mouse',
            'Inndy', 'Jenny', 'HackNTU 總召', '蟆總統', '王立委'
        ])

    def company(self):
        return random.choice([
            'Elppa', 'Alset', 'MBI', 'LargeHard',
            'Elcaro', 'Allizom', 'Edonil', 'SUSA',
            'Reca', 'Elgoog', 'Letin', 'CafeGot',
            '大硬鐵門'
        ])

    def product(self):
        return random.choice([
            'CamKoob', 'PhoneI', 'Suxen', 'TenPhone',
            '個資', '雲端平台', '開發版', '作業系統',
            '作業系統'
        ])

    def buzz(self):
        return random.choice([
            '雲端', '物連網', '大數據', '機器學習', '深度學習',
            '駭客', '創業', '開源', '資料探勘', '敏捷開發', '矽谷'
        ])

    def topic(self):
        return ''.join(set(self.buzz() for _ in range(4)))

    def title(self):
        return random.choice([
            '十億人都驚呆了！%s憑空產生能源' % self.company(),
            '%s 推出新款 %s，完全開源！' % (self.company(), self.product()),
            '%s 宣布，%s旗下%s即將開源' % (self.who(), self.company(), self.product()),
            '%s %s即將全面開源？！' % (self.company(), self.product())
        ])

    def text(self):
        pass

if __name__ == '__main__':
    p = DataProvider()
    print('Topic = %s' % p.topic())
    print('Topic = %s' % p.topic())
    print('Topic = %s' % p.topic())
    print('Topic = %s' % p.topic())
    print('Title = %s' % p.title())
    print('Title = %s' % p.title())
    print('Title = %s' % p.title())
    print('Title = %s' % p.title())
    print('Title = %s' % p.title())
    print('Title = %s' % p.title())
