import time

def get_thread(thread_name):
    time.sleep(1)
    print(f'{thread_name}')

list = ['one', 'two', 'three', 'four', 'five']

for i in list:
    get_thread(i)



