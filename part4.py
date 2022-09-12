import requests
import time
from threading import Thread
from datetime import datetime

start_time = datetime.now()
def get_html(link):
    time.sleep(2)
    res = requests.get(link)
    print(res)

list1 = ['https://www.digitalocean.com/community','https://google.ru', 'https://yandex.ru', 'https://ru.wikipedia.org','https://github.com/PaulinKingsly/module_6' ]

threads = [Thread(target= get_html, args=(i, )) for i in list1]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(datetime.now() - start_time)