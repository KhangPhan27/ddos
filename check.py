import time
import requests
import threading
import os
from termcolor import colored
from colorama import init, Fore, Back, Style
os.system("clear")
url=input('URL:')
thread=int(input('Thread:'))
os.system("clear")
def request_10000_async():
    start = time.perf_counter()
    client = requests.Session()

 
    	
    def requestpost(secret_number):
        client.post(url.format(secret_number))
        req=requests.get(url).status_code
        if req==200:
        	print(Fore.WHITE+'Status code:', req,' Method:GET')
        else:
        	 print(Fore.RED+'Status code:', req,' Method:GET')
    def request(secret_number):
        client.get(url.format(secret_number))
        req=requests.get(url).status_code
        if req==200:
        	print(Fore.WHITE+'Status code:', req,' Method:POST')
        else:
        	 print(Fore.RED+'Status code:', req,' Method:POST')
     


    tasks = []
    
    for secret in range(thread):
        # Tạo thread và khởi động chúng
        task = threading.Thread(target=request, args=(secret,))       
        task.start()
        tasks.append(task)
        rq2 = threading.Thread(target=requestpost, args=(secret,))        
        rq2.start()
        tasks.append(rq2)
    
    # Đợi tất cả thread thực thi xong
    
request_10000_async()