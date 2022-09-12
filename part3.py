import requests
import time
from datetime import datetime

start_time = datetime.now()
def get_html(link):
    time.sleep(2)
    res = requests.get(link)
    print(res)


get_html('https://www.digitalocean.com/community')
get_html('https://google.ru')
get_html('https://yandex.ru')
get_html('https://ru.wikipedia.org')
get_html('https://github.com/PaulinKingsly/module_6')

print(datetime.now() - start_time)



