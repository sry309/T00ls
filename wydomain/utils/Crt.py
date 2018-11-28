import re
import json
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from config import *


class search_crt(object):
    def __init__(self,doamin):
        self.domain = doamin
        self.url = "https://crt.sh/"

    def run(self):
        try:
            url = '{0}?q=%.{1}&output=json'.format(self.url,self.domain)
            r = requests.get(url)
            if r.status_code != 200:
                print '[X] Information not available!'
                exit(1)
            
            json_data = json.loads('[{}]'.format(r.text.replace('}{', '},{')))
            for (key,value) in enumerate(json_data):
                if is_domain(value['name_value']):
                    print(value['name_value'])
        except Exception as e:
            print e