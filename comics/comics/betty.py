from comics.aggregator.crawler import BaseComicsComComicCrawler
from comics.meta.base import BaseComicMeta

class ComicMeta(BaseComicMeta):
    name = 'Betty'
    language = 'en'
    url = 'http://comics.com/betty/'
    start_date = '1991-01-01'
    history_capable_date = '2008-10-13'
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = -5
    rights = 'Delainey & Gerry Rasmussen'

class ComicCrawler(BaseComicsComComicCrawler):
    def crawl(self):
        self.crawl_helper('Betty')
