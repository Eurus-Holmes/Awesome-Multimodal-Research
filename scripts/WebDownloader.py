# -*- coding:utf-8 -*- 
import re
from pprint import pprint
import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        html = requests.get(url).text
    except Exception as e:
        print('web requests url error: {}\nlink: {}'.format(e, url))
    return html


class WebDownloader(object):

    def __init__(self, base_url):
        self.url = base_url
        self.links = set()

    def parse_html(self, verbose=False):
        html = get_html(self.url)
        soup = BeautifulSoup(html, parser='lxml')
        for link in soup.findAll('a'):
            if link.has_attr('href'):
                href = str(link.get('href'))
                if href.startswith('http'):
                    self.links.add(href)
                    if verbose:
                        print(link.get('href'))

    def download(self):
        for link in self.links:
            link = str(link)
            if link.endswith('.pdf'):  # handle direct pdf url link
                file_name = link.split('/')[-1]
                try:
                    r = requests.get(link)
                    # with open(os.path.join(path, file_name), 'wb+') as f:
                    with open(file_name, 'wb+') as f:
                        f.write(r.content)
                except Exception as e:
                    print('Downloading error:{}\nlink:{}'.format(e, link))


url = 'https://chenfeiyang.top/Awesome-Multimodal-Research/'
wd = WebDownloader(url)
wd.parse_html()
pprint(wd.links)
wd.download()
