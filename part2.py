import time
from threading import Thread
from datetime import datetime

start_time = datetime.now()

def get_thread(thread_name):
    time.sleep(1)
    print(f'{thread_name}')

list1 = ['one ', 'two ', 'three ', 'four ', 'five ']

threads = [Thread(target=get_thread, args=(i , )) for i in list1]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(datetime.now() - start_time)