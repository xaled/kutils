import logging
logging.basicConfig()
from kutil.crawler import Crawler
from kutil.urlselector.ratequeue import RateQueue

count =0
def callback(url, response):
    global count
    count += 1
    print count, ">", url, len(response.text), 'bytes'

crawler = Crawler(['http://www.hespress.com'], callback=callback, maxdepth=2, maxurls=20, urlselector=RateQueue())
crawler.join()