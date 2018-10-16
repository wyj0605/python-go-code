#coding: utf-8
import urllib,socket,re,urllib2,httplib,os,string,sys,time
from bs4 import BeautifulSoup
import threading
import thread
lock = thread.allocate_lock()
import Queue
import time
import datetime
qq = Queue.Queue()
q = Queue.Queue()
type2 = sys.getfilesystemencoding()
def filter_tags(htmlstr):	#先过滤CDATA
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_br=re.compile('<br\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    s=re_cdata.sub('',htmlstr)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    s=re_br.sub('\n',s)#将br转换为换行
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释#去掉多余的空行
    blank_line=re.compile('\n+')
    s=blank_line.sub('\n',s)
    return s
def c2(cl):
           reg=r'http://.*?\.html/2'         
           c1l=list(set(re.compile(reg).findall(cl)))
           if c1l:
                for pp in c1l:
                    content=urllib.urlopen(pp)
                    content=content.read()
                    soup=BeautifulSoup(content,"lxml")
                    ct=str(soup.find('div',{"class":"entry-content"}))
                    ct=cl+ct
                    return ct
           else:
                return cl
            
def listurl():
    cl=q.get()
    global lock
    if cl :
           content=urllib.urlopen(cl).read()
           soup=BeautifulSoup(content,"lxml")
           title=str(soup.html.title)
           title=((filter_tags(title)).split('|'))[0]
           title="<h1>"+title+"</h1>"
           cl=str(soup.find('div',{"class":"grap"}))
           c3=c2(cl)
           lock.acquire() #创建锁
           fname="/zuoan.html"
           fp=open(fname,'a')
           fp.write(title)
           print title
           fp.write(c3)
           fp.close()
           lock.release() #释放锁

def open1(url1):
           headers = {  
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
           }  
           req = urllib2.Request(  
                url = url1,  
                headers = headers  
          )  
           content = urllib2.urlopen(req).read()
           return content

def urlzs():
    for k in range(1,5):
           url="http://www.zreading.cn/page/"+str(k)
           qq.put(url)
           print url
           content=open1(url)
           soup=BeautifulSoup(content,"lxml")
           cl=str(soup.find('div',{"class":"layoutMultiColumn--primary"}))
           reg=r'http://.*?\.html'
           cl=re.compile(reg).findall(cl)
	   print cl
           for i in cl:
                   q.put(i)
           for k in range(10):
                    new_thread = threading.Thread(target=listurl)
                    new_thread.start()
def main():
        urlzs()   
if __name__ == '__main__':
	main()
