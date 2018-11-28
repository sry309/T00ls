import sys
import argparse

from utils.Alexa import search_Alexa
from utils.Crt import search_crt
from utils.Ilink import search_ilink
from utils.threatminer import search_threatminer
from utils.threatcrowd import search_threatcrowd
from utils.GoogleSSLdomainFinder import search_GoogleSSLdomainFinder
from utils.findsubdomains import search_findsubdomains

def main(args):
    domain = args.domain

    if not domain:
        print('usage: wydomain.py -d Google.com')
        sys.exit(1)

#    result = search_Alexa(domain).run()
    
#    result = search_crt(domain).run()

#    result = search_ilink(domain).run()

#    result = search_threatcrowd(domain).run()

#    result = search_threatminer(domain).run()

#    result = search_GoogleSSLdomainFinder().run(domain)

#    result = search_findsubdomains(domain).run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="subdomains")
    parser.add_argument("-d","--domain",metavar="",help="domain name")
    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        print "Ctrl C - Stopping Client"
        sys.exit(1)