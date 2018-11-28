import re
import requests
import json
import time
from config import *

class search_threatcrowd(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = 'https://www.threatcrowd.org/'

    def run(self):
        url = '{0}/searchApi/v2/domain/report/?domain={1}'.format(self.url,self.domain)
        time.sleep(10)
        r = requests.get(url).text
        print r
        for sub in json.loads(r).get("subdomains"):
            if is_domain(sub):
                print(sub)