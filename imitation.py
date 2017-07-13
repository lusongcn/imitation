# -*- coding: utf-8 -*-
import urllib2
import urllib
import requests
import re
import sys
import config
from urlparse import *
import os
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup

class Imitation(object):
    def __init__(self):
        self.headers = {'Referer':'https://www.baidu.com/','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

    def main(self,handle):
        if handle != "end":
            if handle[0] == "single":
                self.hand(handle[1])
            else:
                lists = self.readLists(handle[1])
                for list in lists:
                    self.hand(list)

    def hand(self,url):
        req = requests.get(url, headers=self.headers)
        status = req.status_code
        if status == 200:
            print "\033[0;33;40m HostUrl：\033[0m"+url
            # 解析网址
            urlparses = urlparse(url)
            # 提取网址
            baseurl = urlparses.netloc
            # 网页前缀
            scheme = urlparses.scheme
            # 给本连接明名
            htmlname = self.htmlName(url)
            self.mkprojectdir(baseurl)
            self.jindu(10)
            self.jindu(20)
            soup = BeautifulSoup(req.text,"html.parser")
            newhtml = self.savescript(scheme,baseurl,soup,req.text)
            self.jindu(30)
            newhtml = self.savePics(baseurl,soup,newhtml,scheme)
            self.jindu(40)
            self.jindu(50)
            self.jindu(60)
            newhtml = self.savecss(scheme,baseurl,soup,newhtml)
            self.jindu(70)
            self.jindu(80)
            self.jindu(90)
            allurl = scheme+"://"+baseurl+"/"
            newhtml = newhtml.replace('href="/','href="').replace('src="/','src="').replace(allurl,'')
            self.writedoc(baseurl,htmlname,newhtml)
            self.jindu(100)
        else:
            print "\033[0;31;40m HostUrl\033[0m"+url

    def readLists(self,file):
        fo = open(file, "r+")
        strs = fo.readlines()
        # 关闭打开的文件
        fo.close()
        return strs

    def savecss(self,scheme,baseurl,soup,html):
        links = soup.find_all(rel="stylesheet")
        for link in links:
            css = link.get("href")

            if css:
                if "http" in css:
                    re_css = css
                else:
                    re_css= scheme+"://"+baseurl+css

                x= css.split('/')
                ncss = "/css/"+x[len(x)-1]
                vcss = re.findall(r"(.*)\?", ncss)
                if vcss:
                    ncss = vcss[0]
                try:
                    cssinfo = requests.get(re_css, headers=self.headers)
                    # 打开一个文件
                    fo = open(baseurl+ncss, "wb+")
                    csshtml = cssinfo.text
                    bkimgs = re.findall(r"background-image: url\((.*)\);", csshtml)
                    if bkimgs:
                        for bkimg in bkimgs:
                            f= bkimg.split('/')
                            nimg = "../images/"+f[len(f)-1]

                            if "http" in bkimg:
                                re_img = bkimg
                            else:
                                simg = bkimg.replace("../","/")
                                ssimg = simg.replace("//","/").replace("///","/")
                                re_img= scheme+"://"+baseurl+ssimg

                            try:
                                newimgsrc = baseurl+'/images/%s' % f[len(f)-1]
                                urllib.urlretrieve(re_img,newimgsrc)
                                csshtml = csshtml.replace(bkimg,nimg)
                            except:
                                errorimg = "Img Save Error"
                    fo.write(csshtml)
                    html = html.replace(css,ncss)
                    # 关闭打开的文件
                    fo.close()
                except:
                    continue

        return html

    def savescript(self,scheme,baseurl,soup,html):
        scripts = soup.find_all("script")
        for script in scripts:
            js = script.get('src')
            if js:
                if "http" in js:
                    re_js = js
                else:
                    re_js = scheme+"://"+baseurl+js

                x= js.split('/')
                njs = "/js/"+x[len(x)-1]
                vjs = re.findall(r"(.*)\?", njs)
                if vjs:
                    njs = vjs[0]

                try:
                    jsinfo = requests.get(re_js, headers=self.headers)
                    # 打开一个文件
                    fo = open(baseurl+njs, "wb+")
                    fo.write(jsinfo.text)
                    html = html.replace(js,njs)
                    # 关闭打开的文件
                    fo.close()
                    html.replace(js,njs)
                except:
                    continue
        return html



    def htmlName(self,requrl):
        resurl = requrl.replace('\t','').replace('\n','').replace(' ','')
        x= resurl.split('/')

        ncss = x[len(x)-1]
        vcss = re.findall(r"(.*)\?", ncss)
        if vcss:
            ncss = vcss[0]

        if ncss:
            if ".html" in ncss:
                return ncss
            else:
                if ".htm" in ncss:
                    return ncss
                else:
                    return ncss+".html"
        else:
            return "index.html"

    def writedoc(self,baseurl,filename,content):
        # 打开一个文件
        fo = open(baseurl+"/"+filename, "wb+")
        fo.write(content)

        # 关闭打开的文件
        fo.close()

    def savePics(self,baseurl,soup,text,scheme):
        allimgs = soup.find_all('img')
        html = text
        for allimg in allimgs:
            link = allimg.get('src')
            if "http" in link:
                newlink = link
            else:
                newlink = scheme+"://"+baseurl+link

            x= link.split('/')
            nimg = "images/"+x[len(x)-1]
            try:
                newimgsrc = baseurl+'/images/%s' % x[len(x)-1]
                urllib.urlretrieve(newlink,newimgsrc)
                html = html.replace(link,nimg)
            except:
                errorimg = "Img Save Error"
        return html


    def mkprojectdir(self,baseurl):
        exists = os.path.exists(baseurl)
        if exists:
            print "\033[0;33;40m Notice：\033[0m"+"Project Exists"
        else:
            os.mkdir(baseurl)
            os.mkdir(baseurl+"/css")
            os.mkdir(baseurl+"/js")
            os.mkdir(baseurl+"/images")

    def jindu(self,n):
        import sys,time
        fmt = '{:3d} [{:<100}]'.format
        print '\r',fmt(n, '='*n)


if __name__ == "__main__":
    imitation = Imitation()
    config = config.imitationConfig()
    handel = config.getInstructions()
    imitation.main(handel)
