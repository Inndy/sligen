import crawlers
import hashlib

c = crawlers.pixabay()
for i in range(300):
    print('Processing image #%d...' % (i+1))
    image_downloader = c.next()
    content = image_downloader()
    checksum = hashlib.md5(content).hexdigest()
    open('data/img/%s.jpg' % checksum, 'wb').write(content)
