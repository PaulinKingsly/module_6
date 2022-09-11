import requests
import time

def get_html(link):
    time.sleep(2)
    res = requests.get(link)
    print(res)

get_html('https://www.digitalocean.com/community')
get_html('https://google.ru')
get_html('https://yandex.ru')
get_html('https://ru.wikipedia.org')
get_html('https://github.com/PaulinKingsly/module_6')



