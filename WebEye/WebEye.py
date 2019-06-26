import requests
import threading


headers = {'Accept' : 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
           }

Storage_Http = []
Storage_Https = []


def Web_Probe():
    for x in open('url.txt').readlines():
        Probe_Http = 'http://' + x.strip()
        Storage_Http.append(Probe_Http)
        Probe_Https = 'https://' + x.strip()
        Storage_Https.append(Probe_Https)



def main_Storage_http():
    for A in Storage_Http:
        try:
            r_http = requests.head(url=A,headers=headers,timeout=10)
            if r_http.status_code != 404:
                print(A,r_http.status_code)
        except Exception as E:
            print(E)

def main_Storage_https():
    for B in Storage_Https:
        try:
            r_https = requests.get(url=B,headers=headers,timeout=10)
            if r_https.status_code != 404:
                print(B,r_https.status_code)
        except Exception as E:
            print(E)


threads = []
t1 = threading.Thread(target=main_Storage_http)
threads.append(t1)
t2 = threading.Thread(target=main_Storage_https)
threads.append(t2)



if __name__ == '__main__':
    Web_Probe()
    for t in threads:
        t.start()
