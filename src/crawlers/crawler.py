class Crawler(object):
    def __init__(self):
        raise NotImplementedError()

    def next(self):
        '''
        return (title, content, images)

        content is a list of all paragraph
        images is a list of all images url
        '''
        raise NotImplementedError()

    def grab(self):
        '''
        grab some data to queue
        '''
        raise NotImplementedError()
