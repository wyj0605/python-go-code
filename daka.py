#-*-coding:utf-8-*-
import requests,json
import random,time
'''
安装FIDDLER抓包工具分析打卡小程序
'''
def url_post():
    url='https://jkm.kaiqun.net/modules/student-clock-in/save'
    body = \
    {
        "typeId":	1,
        "typeName":	"日常打卡",
        "clockByUserRelation":	"爸爸",
        "isolate":	0,
        "epidemicId":	1,
        "epidemicName":	"无新冠肺炎",
        "inThisCity":	1,
        "inEpidemicCityId":	0,
        "inEpidemicCityName":	"否",
        "livingInSchool":	0,
        "attendanceId":	1,
        "attendanceName":	"已开学",
        "symptomId":	0,
        "symptomIds":	0,
        "symptomNames":	"自觉正常",
        "symptomResult":	0,
        "ext01":	"8小时以下",
        "corpId":	"微信用户ID",#抓包工具分析出微信用户ID
        "userId":	"2-2-5"
    }
    headers = {
        'Authorization':'',#抓包分析出authorization
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030073)',
        'Referer':'https://jkm.kaiqun.net/index.html?code=v5BbtyGwAV21NseHiD29FPyo73g2rx_y2oyfNHkF2Bw&state=STATE'}
    req = requests.post(url, headers= headers,data=body)
    return req.json()

print(url_post())


