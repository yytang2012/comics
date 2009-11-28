from comics.aggregator.crawler import BaseComicCrawler
from comics.meta.base import BaseComicMeta

class ComicMeta(BaseComicMeta):
    name = 'Rocky (db.no)'
    language = 'no'
    url = 'http://www.dagbladet.no/tegneserie/rocky/'
    start_date = '1998-01-01'
    history_capable_days = 14
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = 1
    rights = 'Martin Kellerman'

class ComicCrawler(BaseComicCrawler):
    def crawl(self):
        self.url = 'http://www.dagbladet.no/tegneserie/rockyarkiv/serve.php?%(date)s' % {
            'date': self.date_to_epoch(self.pub_date),
        }
