import requests,re,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from requests.packages.urllib3.exceptions import ConnectionError

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    'Accept': 'Encoding:gzip, deflate',
    'Accept': 'Language:en, zh - CN',
    'Referer': 'http://maoyan.com/board/4?'
}

def get_proxy():
    try:
        t = requests.get("http://10.10.1.204:80/get")
        if 200 == t.status_code:
            proxy = {'http': t.text}
            return proxy
        return None
    except ConnectionError:
        t = requests.get("http://10.10.1.204:80/get")
        proxy = {'http': t.text}
        return proxy


for i in range(1, 10):
    t = requests.get('http://maoyan.com/board/4?offset=' + str(i * 10), proxies=get_proxy(), headers=headers)
    part = re.compile(
        '<dd>.*?<i.*?<a href=".*?" title="(.*?)" class=.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
        re.S)
    items = re.findall(part, t.text)
    for item in items:
        t = item[0] + item[1].split()[0] + item[2]
        with open('1.txt', 'a') as f:
            f.write(t + '\n')
