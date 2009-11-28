from comics.aggregator.crawler import BaseComicCrawler
from comics.meta.base import BaseComicMeta

class ComicMeta(BaseComicMeta):
    name = 'Deep Fried'
    language = 'en'
    url = 'http://www.whatisdeepfried.com/'
    start_date = '2001-09-16'
    history_capable_days = 14
    schedule = 'Mo,Tu,We,Th,Fr,Sa'
    time_zone = -5
    rights = 'Jason Yungbluth'

class ComicCrawler(BaseComicCrawler):
    def crawl(self):
        self.parse_feed('http://www.whatisdeepfried.com/feed/')

        for entry in self.feed.entries:
            if self.timestamp_to_date(entry.updated_parsed) == self.pub_date:
                self.title = entry.title
                pieces = entry.summary.split('"')
                for i, piece in enumerate(pieces):
                    if piece.count('src='):
                        self.url = pieces[i + 1]
                        return
