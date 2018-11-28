from lib.GSDFA import GoogleSSLdomainFinder
from config import *
import urllib3
urllib3.disable_warnings()


class search_GoogleSSLdomainFinder(object):
    def run(self,args):
        domain = GoogleSSLdomainFinder('{0}'.format(args),'show')
        for subs in domain.list():
            if is_domain(subs):
                print subs