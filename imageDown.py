# -*- coding: utf-8 -*-
import requests
import re
import os



downloadDirPath = '/Users/tangmengbo/Desktop/download'#下载下来图片要保存到的文件夹路径

#'Host': 'tieba.baidu.com',
webHeaders = {'Host': 'tieba.baidu.com',
'method': 'GET',
'path': '/question/27364360',
'scheme': 'https',
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'cookie': 'TIEBA_USERTYPE=6e38cd16e89501afe2f17ce4; FP_UID=88cd11aa371a693bafd977c8950b1f01; PSTM=1508392484; BIDUPSID=7DFA1B875D5271A5BAAA5561AA5918E6; BAIDUID=E8466CF472ECBD1C3AFE02033D3B0EC8:FG=1; FP_LASTTIME=1508484287746; TIEBAUID=cb23caae14130a0d384a57f1; H_PS_PSSID=1435_25810_21096_20929; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; wise_device=0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1521629325; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1521629325',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'

}#获取网页源码时设置,防止抓取不到
heards = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}#图片写入文件夹时设置,避免下载下来图片打不开


#获取url对应的网页源码
def getHtmlText(url):
    try:
        resp = requests.get(url,headers=webHeaders)
        print(resp.encoding+'\n\n')
        return resp.text
    except:
        print('haha')
        return 'qwer'

#解析url源码页面获取图片路径的数组
def getUrlsFromHTML(html):
    reg = r'src="(http[^;]+?\.[jpg][pin][egf]g*)'#正则表达式含义:以http开头,以jpg或png结尾中间是除了;的任意字符的字符串
    imgre = re.compile(reg)
    #reg=re.compile(pattern)
    urls=imgre.findall(html)
    return urls

i=0
#下载图片
def download(List):
    global i
    for url in List:
        r=requests.get(url,headers=heards,timeout=30)#headers防止图片下载下来后打不开
        r.encoding=r.apparent_encoding
        if not os.path.exists(downloadDirPath):#判断downloadDirPath下的文件夹是否存在不存在择创建
            os.makedirs(downloadDirPath)
        if '.png' in url:#根据图片路径判断图片的格式并在给下载下来的图片命名时使用
            path = downloadDirPath+'/'+str(i)+'.png'#图片要下载到的文件夹路径和图片名组合成图片的保存路径
        elif '.jpg' in url:
            path = downloadDirPath+'/'+str(i)+'.jpg'
        else:
            path = downloadDirPath+'/'+str(i)+'.gif'
        if not os.path.exists(path):
            with open(path,'wb') as f:
                f.write(r.content)#网文件夹中写入图片
                f.close()
                print(str(i)+' 文件保存成功')
        else:
            print('文件已经存在')
        i+=1

def main(url):
    html = getHtmlText(url)
    urls = getUrlsFromHTML(html)
    for str in urls :#循环打印图片地址
        print(str+'\n')
    download(urls)
#一个帖子可能有很多页这里举一个两页帖子的例子,for循环一页一页进行下载
for index in range(1,4):#range(n,m)从n开始到m不包含m
    print('\n'+'第'+str(index)+'页图片下载')
    url = 'https://tieba.baidu.com/p/5865427389'#要抓取图片的网址
    url = url+'?pn='+str(index)
    print(url)
    main(url)


