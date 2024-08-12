import requests

cookies = {
    '_ga': 'GA1.1.200664832.1711456901',
    'yrm': 'true',
    'ASPSESSIONIDCGSRBTCB': 'OLGBNKMAMOIHIMMGOPGFAKGN',
    'ASPSESSIONIDQUTRCTAA': 'ANHAMOABJDFBJEDAGEDKMAKK',
    '_ga_GRD9HD6XEV': 'GS1.1.1711456900.1.1.1711456932.28.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.1.200664832.1711456901; yrm=true; ASPSESSIONIDCGSRBTCB=OLGBNKMAMOIHIMMGOPGFAKGN; ASPSESSIONIDQUTRCTAA=ANHAMOABJDFBJEDAGEDKMAKK; _ga_GRD9HD6XEV=GS1.1.1711456900.1.1.1711456932.28.0.0',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

from bs4 import BeautifulSoup
import time as t

class KurKontrol():
    def MainControl(kur_id):
        while True:
            response = requests.get('https://altin.in', cookies=cookies, headers=headers)
            if(response.status_code == 200):
                source = BeautifulSoup(response.content, "html.parser")
                return source.find("div", attrs={"id":kur_id}).find("h2").text
            else:
                # print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + " " + "Sayfa engellemesi")
                t.sleep(0.5)
    
    def Dolar():
        return '\U0001F4B2 ' + KurKontrol.MainControl("dolar")
        
    def Altin():
        return '\U0001F4AA ' + KurKontrol.MainControl("ons")
        
    def Euro():
        return '\U0001F4B6 ' + KurKontrol.MainControl("euro")
        
    def Parite():
        return '\U0001F500 ' + KurKontrol.MainControl("parite")
        
    def Gumus():
        return '\U0001F48D ' + KurKontrol.MainControl("gumus")
        
    def Platin():
        return '\U0001F494 ' + KurKontrol.MainControl("platin")











# print(response.text)