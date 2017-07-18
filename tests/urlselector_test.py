from kutil.urlselector import UrlSelector
from kutil.urlselector.ratequeue import RateQueue
import time
import cProfile

links = ['http://www.zone-h.org/archive', 'http://alternativeto.net/software/stumbleupon/?license=opensource',
         'https://sourceforge.net/projects/semanticscuttle/',
         'https://www.google.com/search?client=ubuntu&channel=fs&q=sorted+tree+python&ie=utf-8&oe=utf-8',
         'https://www.google.com/search?client=ubuntu&channel=fs&q=sorted+tree+python&ie=utf-8&oe=utf-8',
         'https://PYPI.python.org/pypi/sortedcontainers',
         'https://pypi.PYTHON.org/pypi/sortedcontainers',
         'https://www.google.com/search?client=ubuntu&channel=fs&q=heap&ie=utf-8&oe=utf-8#channel=fs&q=worker+queue+design+pattern',
         'https://www.google.com/search?client=ubuntu&channel=fs&q=design+patterns&ie=utf-8&oe=utf-8#channel=fs&q=+design+patterns+programming',
         'https://sourcemaking.com/design_patterns', 'http://www.oodesign.com/',
         'http://www.tutorialspoint.com/design_pattern/', 'https://en.wikipedia.org/wiki/K-means_clustering',
         'https://en.wikipedia.org/wiki/Edit_distance',
         'https://www.reddit.com/r/algorithms/comments/4l9mxh/my_uncles_factorization_algorithms/',
         'https://www.reddit.com/r/coolgithubprojects/top/?sort=top&t=month',
         'https://github.com/smoqadam/PyFladesk', 'https://github.com/smoqadam/PyFladesk-rss-reader',
         'https://www.reddit.com/r/help/comments/ygm0y/xpost_what_is_it_and_how_do_i_do_it/',
         'https://github.com/daoudclarke',
         'https://www.google.com/search?client=ubuntu&channel=fs&q=Daoud+Clarke&ie=utf-8&oe=utf-8',
         'http://www.scrabblist.com/', 'http://daoudclarke.github.io/machine-learning-practice.html',
         'http://getbootstrap.com/2.3.2/javascript.html#overview', 'http://jekyllbootstrap.com/',
         'http://daoudclarke.github.io/guide.pdf', 'http://thewatchseries.to/episode/scrubs_s8_e3.html',
         'http://stackoverflow.com/questions/120951/how-can-i-normalize-a-url-in-python',
         'https://gist.github.com/mnot/246089#file-urlnorm-py',
         'http://stackoverflow.com/questions/1307014/python-str-versus-unicode',
         'http://www.habous.gov.ma/%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D9%8A%D8%A9-%D8%A7%D9%84%D8%B4%D8%A4%D9%88%D9%86-%D8%A7%D9%84%D8%A5%D8%B3%D9%84%D8%A7%D9%85%D9%8A%D8%A9.html',
         'http://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints']
extralink = "http://stackoverflow.com/users/15842/gregg-lind"

def test_selector(selector):
    #print len(links)
    #t0 = time.time()
    for l in links:
        selector.put(l)
    #t1 = time.time()
    #print "put: %fs"%(t1-t0)

    #selector.put(extralink)
    #t2 = time.time()
    #print "put1: %fs"%(t2-t1)

    while len(selector) >0:
        selector.pop()
    #t3 = time.time()
    #print "pop: %fs"%(t3-t2)

def main1():
    for i in range(10):
        test_selector(UrlSelector())

def main2():
    for i in range(10):
        test_selector(RateQueue())

if __name__ == "__main__":
    cProfile.run('main1()')
    cProfile.run('main2()')

