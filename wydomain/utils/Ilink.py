import re
import requests

from config import *

class search_ilink(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = 'http://i.links.cn/subdomain/'

    def run(self):
        try:
            payload = {
                'b2': 1,
                'b3': 1,
                'b4': 1,
                'domain': self.domain
            }
            r = requests.post(self.url,data=payload).text
            subs = re.compile(r'(?<=value\=\"http://).*?(?=\"><input)')
            for item in subs.findall(r):
                if is_domain(item):
                    print(item)
        except Exception as e:
            print(e)