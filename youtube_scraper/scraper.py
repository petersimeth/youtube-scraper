""" Library entry point """
import requests
from bs4 import BeautifulSoup

class YoutubeScrape(object):
    """ Scraper object to hold data """
    def __init__(self, soup):
        """ Initialize and scrape """
        self.soup = soup
        self.title = self.parse_string('.watch-title')
        self.poster = self.parse_string('.yt-user-info')
        self.views = self.parse_int('.watch-view-count')
        self.published = self.parse_string('.watch-time-text').replace('Published on ', '')
        self.like = self.parse_int('#watch-like')
        self.dislike = self.parse_int('#watch-dislike')

    def parse_int(self, selector):
        """ Extract one integer element from soup """
        return int(self.parse_string(selector).replace(',', ''))

    def parse_string(self, selector):
        """ Extract one particular element from soup """
        return self.soup.select(selector)[0].get_text().strip()


def scrape_html(html):
    """ Return meta information about a video """
    return YoutubeScrape(BeautifulSoup(html))


def scrape_url(url):
    """ Scrape a given url for youtube information
    Should match '(youtu\.be/|youtube\.com/watch?v=)[\S]+' """
    html = requests.get(url).text
    return scrape_html(html)
