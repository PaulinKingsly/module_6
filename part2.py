import time
from threading import Thread

def get_thread(thread_name):
    time.sleep(1)
    print(f'{thread_name}')

list = ['one', 'two', 'three', 'four', 'five']

threads = [Thread(target= get_thread, args= (list, ))]
for t in threads:
    t.start()

for t in threads:
    t.join()

# В threads  в качестве аргумента указан list, поэтому в итоге программа выводит весь список целиком. Как правильно
# указать аргумент, чтобы отдельно выводился каждый элемент списка?