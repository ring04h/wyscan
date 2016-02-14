# coding: utf-8

import sys
from concurrent import futures
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

URLS = ['http://www.baidu.com/',
        'http://www.qq.com/',
        'http://www.sina.com.cn',
        'http://www.163.com',
        'http://mail.163.com']

def load_url(url):
    return requests.get(url).content

with futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = dict((executor.submit(load_url, url), url) for url in URLS)

    for future in futures.as_completed(future_to_url):
        url = future_to_url[future]
        if future.exception() is not None:
            print('%r generated an exception: %s' % (url,future.exception()))
        else:
            print('%r page is %d bytes' % (url, len(future.result())))