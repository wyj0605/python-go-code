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
def filter_tags(htmlstr):
	#先过滤CDATA
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

def listurl():
    cl=q.get()
    global lock
    try:
        
        if cl :
               content=open1(cl)
               soup=BeautifulSoup(content,fromEncoding="gbk")
               title=str(soup.html.title)
               title=((filter_tags(title)).split('-'))[0]
               print title
               title="<h1>"+title+"</h1>"
               cl=str(soup.find('div',{"class":"Blog_wz1"}))
               cl=cl.replace('/attachment','http://blog.itpub.net/attachment')
               fname="D://temp//"+str(down_name)+".html"
               fp=open(fname,'a')
               fp.write(title)
               #print title+'\n'
               #print cl
               fp.write(cl)
               fp.close()
    except Exception as e:
          print e
def open1(url1):
                  
           headers = {  
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
           }  
           req = urllib2.Request(  
                url = url1,  
                headers = headers  
          )  
           content = urllib2.urlopen(req).read()
           #print content
           return content

def urlzs():
    for k in range(1,down_int):
           url='http://blog.itpub.net/'+str(list_num)+'/abstract/'+str(k)+'/' 
           print url 
           content=open1(url) 
           
           soup=BeautifulSoup(content)
           cl=str(soup.find('div',{"class":"Blog_right1"}))
           csdnreg=r'\d{4,9}/viewspace-\d{3,9}/'
           cl=list(set(re.compile(csdnreg).findall(cl)))
           print cl
           for i in cl:
               q.put('http://blog.itpub.net/'+i)
               # listurl(i)
           for k in range(10):
                new_thread = threading.Thread(target=listurl)
                new_thread.start()
           print url
def main():
        urlzs()   
if __name__ == '__main__':
        global down_int
        global down_name
        global list_num
        url='http://blog.itpub.net/14710393/abstract/1/'
        content=open1(url)
        list_num=((url).split('/'))[-4]
        print list_num
        soup=BeautifulSoup(content)
        title=str(soup.html.title)
        title=((filter_tags(title)).split('-'))[0]
        down_name=((filter_tags(title)).split('_'))[-1]
        print down_name
        cl=str(soup.find('li',{"class":"last"}))
        down_int=int(((cl).split('/'))[-4])
        print down_int
        urlzs()
