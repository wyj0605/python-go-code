#coding: utf-8
import os,urllib2,time,sys  
import urllib  
import httplib
import json
#from wx import wx1

def get_token():  
        apiKey = ""  #申请百度AI帐号,并新建应用文字转语音
        secretKey = ""  
        auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey; 
        res = urllib2.urlopen(auth_url)  
        json_data = res.read()  
        t=str(json.loads(json_data)['access_token'])
        return t
def weather():
		httpClient = None 
		httpClient = httplib.HTTPConnection('api.map.baidu.com', 80, timeout=30)
		httpClient.request('GET', '/telematics/v3/weather?location=哈尔滨&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback=')
		response = httpClient.getresponse()   
		s = json.loads(response.read());
		city=u"  "+s["results"][0]["currentCity"]+u"市，"
		date1=s["results"][0]["weather_data"][0]["date"]+u"，"
		weather_day=s["results"][0]["weather_data"][0]["weather"]+u"，"
		wind=u"风力: "+s["results"][0]["weather_data"][0]["wind"]+u"。"+"\n"
		temp=u"全天温度: "+s["results"][0]["weather_data"][0]["temperature"]+u"，"
		pm25=u"pm2.5:"+s["results"][0]["pm25"]+u"，"
		chuanyi=u"穿衣提示: "+s["results"][0]["index"][0]["des"]+"\n"
		xiche=u"洗车提示: "+s["results"][0]["index"][1]["des"]+"\n"
		yundong=u"运动提示: "+s["results"][0]["index"][3]["des"]+u"。"+"\n"
		r=s["results"][0]["weather_data"][1]["date"]+u"，"
		f=s["results"][0]["weather_data"][1]["weather"]+u"，"
		w=s["results"][0]["weather_data"][1]["temperature"]+u"，"
		wind1=s["results"][0]["weather_data"][1]["wind"]+u"。"
		wind2=s["results"][0]["weather_data"][2]["wind"]+u"。"
		r1=s["results"][0]["weather_data"][2]["date"]+u"，"
		f2=s["results"][0]["weather_data"][2]["weather"]+u"，"
		w2=s["results"][0]["weather_data"][2]["temperature"]+u"，"
		m1=r+f+w+wind1+"\n"
		m2=r1+f2+w2+wind2+"\n"
		wanbi=u"播报完毕，祝您心情愉快。"
		title=u"天气预报: "
		t=city+date1+weather_day+temp+pm25+wind+m1+m2
	#	wx1(title,t)
		print t
		#file='http://tsn.baidu.com/text2audio?tex='+t.encode("utf-8")+'&lan=zh&per=0&cuid=00-E0-4C-13-DC-A9&ctp=1&tok='+get_token() #文字转语音
		#print file

def main():
        weather()

if __name__ == '__main__':
	main()
