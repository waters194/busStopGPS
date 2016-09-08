# -*- coding: UTF-8 -*-
__author__ = 'Administrator'



import xlrd
import xlwt
import requests
import urllib
import math
import re
import json
import string
import codecs
import sys




def get_station(i):         #抓取一个公交站站名、经纬度
    station=[]
    bus_sto=urllib.quote(u'公交站'.encode('utf8'))               #将关键字转换为utf-8格式
    city=urllib.quote(u'杭州'.encode('utf8'))                    #将搜索范围转换为utf-8格式
    # url1="http://api.map.baidu.com/place/v2/search?ak=ERmrlS13IP07dT4XADfB83IA&output=json&query=%s&scope=1&region=%s&page_size=1&page_num=%d"%(bus_sto,city,i)
    # url1="http://api.map.baidu.com/place/v2/search?ak=ERmrlS13IP07dT4XADfB83IA&output=json&query=%s&scope=1&location=30.326464,120.1675&radius=200000&&page_size=1&page_num=%d"%(bus_sto,i)

    #以某点为圆心
    url1="http://api.map.baidu.com/place/v2/search?ak=ERmrlS13IP07dT4XADfB83IA&output=json&query=%s&scope=1&location=30.259789,120.172214&radius=200000&&page_size=1&page_num=%d"%(bus_sto,i)

    print url1
    req=requests.get(url1)                                  #请求百度地图Place API返回数据
    content= req.content
    data=json.loads(content)                    #将获取的信息封装为字典
    station.append(data['total'])              #提取公交站总数
    result=data['results']                   #提取字典中的有效信息
    try:
      str_temp=result[0]          #保存总数到链表第一个元素
    except:
        station.append('n')
        return station
    loc=str_temp['location']    #提取包含站名、经纬度的字典
    lng=float(loc['lng'])        #提取包含经纬度的字典
    lat=float(loc['lat'])
    station.append(str_temp['name']+",%f"%lng+",%f"%lat)    #将站名、经纬度写入链表
    print station[1]
    return station



def run():                              #开始抓取文件
   reload(sys)
   sys.setdefaultencoding( "utf-8" )
   get_num=get_station(0)               #提取公交站总数
   num=get_num[0]
   for i in range(0,num):           #依次抓取全市所有公交站站名、经纬度,并写入文件保存
    Bstation=get_station(i)
    name_f=file('e:/bus_stop2.txt','a')

    name_f.write(Bstation[1]+'\n')
    name_f.close()                      #关闭文件









if __name__=='__main__':
    run()
