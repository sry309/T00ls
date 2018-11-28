import requests
import re

from config import *

class search_Alexa(object):
    def __init__(self,domain):
        self.domain = domain
        self.url = "http://alexa.chinaz.com/"

    def run(self):
        url = '{0}?domain={1}'.format(self.url,self.domain)
        try:
            r = requests.get(url).text
            subs = re.compile(r'(?<="\>\r\n<li>).*?(?=</li>)')
            result = subs.findall(r)
            for sub in result:
                if is_domain(sub):
                    print sub
        except Exception as e:
            print e
