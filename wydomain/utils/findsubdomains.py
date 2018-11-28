import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

class search_findsubdomains(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = 'https://findsubdomains.com/subdomains-of/'

    def run(self):
        url = '{0}{1}'.format(self.url,self.domain)
        content = requests.get(url).text
        soup = BeautifulSoup(content,'lxml')
        divs = soup.find_all(class_="js-domain-name domains")
        for sub in divs:
            print sub.get_text().strip()