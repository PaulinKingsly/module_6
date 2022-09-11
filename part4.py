import requests
import time
from threading import Thread

def get_html(link):
    time.sleep(2)
    res = requests.get(link)
    print(res)

threads = [Thread(target= get_html, args= # ????)]

for t in threads:
    t.start()
for t in threads:
    t.join()

get_html('https://www.digitalocean.com/community')
get_html('https://google.ru')
get_html('https://yandex.ru')
get_html('https://ru.wikipedia.org')
get_html('https://github.com/PaulinKingsly/module_6')

#При последовательном запуске все работает. При параллельном та же проблема, что и в предыдущем задании.
#Как указать аргументы?