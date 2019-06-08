import requests
import asyncio
from pyppeteer import launch

headers = {'Accept' : 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}

class WebEye:
    def __init__(self):
        blist = []
        f = open('url.txt').readlines()
        for x in f:
            url = x.strip()
            blist.append(url)
            self.blist = blist

    def Html_s(self):
        GEN_HTML = 'ce.html'
        f = open(GEN_HTML,'w')
        str_d = '''
        <meta charset='UTF-8'>
        <style>td {text-align:center}</style>
        <table border="1" cellpadding="3" cellspacing="0" style="width: 80%;margin:auto">
        <tr>
        <td><b><font color="blue">url</font></b></td>
        <td><b><font color="blue">title</font></b></td>
        <td><b><font color="blue">PNG</font></b></td>
        '''
        f.write(str_d)
        f.close()

    def Verify_Page(self):

        result_200 = []

        for i in self.blist:
            url_1 = 'http://' + i
            url_2 = 'https://' + i
            try:
                req_http = requests.head(url=url_1,headers=headers,timeout=10)
                if req_http.status_code != 404:
                    result_200.append(url_1)
                    print(url_1)
            except Exception as e:
                pass
        
            try:
                req_https = requests.head(url=url_2,headers=headers,timeout=10)
                if req_https.status_code != 404:
                    result_200.append(url_2)
                    print(url_2)
            except Exception as e:
                pass

        try:
            async def main():
                browser = await launch(headers=False)
                page = await browser.newPage()
                Page = 0
                for x in result_200:
                    Page += 1
                    try:
                        await page.goto(x,timeout=100000)
                    except Exception as e:
                        pass
                    await page.waitFor(10000)
                    await page.screenshot({'path':'{0}.png'.format(Page)})
                    title = await page.title()
                    report = open('ce.html','a',encoding='utf-8')
                    falg = '''
                    <tr>
                        <td>
                            <font color="blue">%s</font>
                        </td>
                        <td>
                            <font color="blue">%s</font>
                        </td>
                        <td>
                            <img src="%s.png" height="200" width="200" />
                        </td>
                    </tr> ''' % (x,title,Page)
                    report.write(falg)
                    report.close()
                await browser.close()
            asyncio.get_event_loop().run_until_complete(main())
        except Exception as e:
            pass


t = WebEye()
t.Html_s()
t.Verify_Page()