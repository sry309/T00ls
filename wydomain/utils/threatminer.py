import re
import requests

from config import *
class search_threatminer(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = 'https://www.threatminer.org'
    
    def run(self):
        try:
            url = '{0}/getData.php?e=subdomains_container&q={1}&t=0&rt=10&p=1'.format(self.url,self.domain)
            r = requests.get(url).text
            _regex = re.compile(r'href=[\'"]?([^\'" >]+)')
            for sub in _regex.findall(r):
                sub = sub.replace('domain.php?q=','')
                if is_domain(sub):
                    print(sub)
        except Exception as e:
            print e