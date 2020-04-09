# Library Import

from bs4 import BeautifulSoup
import requests
import random

# Helper Definition

# Headers list for random User-Agent to bypass web scraping blocker
headers_list = ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
                "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.116"
               ]

# Web Scraping class

class webscrap:

    # Initializer / Instance Attributes
    def __init__(self, url):
        self.url = url

    # Start web scraping session
    def start(self, random_headers = False):

        if random_headers:
            header = {'User-Agent': random.choice(headers_list) }
        else:
            header = {'User-Agent': headers_list[0]}
        self.response = requests.get(self.url, headers = header)
        code = self.response.status_code    
        if code == 200:
            # print("Connect successfully1")
            pass
        else:
            print(f"{code} Error! Not well connected!")
        return None
    
    # Grab index table in page as a list
    def get_table(self, index = 0):
        soup = BeautifulSoup(self.response.content, 'html.parser')
        t1 = soup.select("table")[index]
        out_lst = []
        for row in t1.find_all("tr"):
            row_lst = []
            for box in row.find_all("td"):
                row_lst.append(box.text)
            out_lst.append(row_lst)
        return out_lst
 
    # Grab url list for given elements and attr
    def get_urls(self, elements = ["ul", "a"], attr='href'):
        soup = BeautifulSoup(self.response.content, 'html.parser')
        out_lst = []
        for a in soup.find_all(elements[0]):
            for b in a.find_all(elements[1]):
                out_lst.append(b.attrs[attr])
        return out_lst
    
    # Grab url list for given elements
    def get_text(self, elements = ["ul", "li"]):
        soup = BeautifulSoup(self.response.content, 'html.parser')
        out_lst = []
        for a in soup.find_all(elements[0]):
            for b in a.find_all(elements[1]):
                out_lst.append(b.text)
        return out_lst