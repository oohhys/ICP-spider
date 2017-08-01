#coding=utf-8
"""
python 3.6
--------------------------------------------
ICP grabber
Author: Vincent
Function: 1.Get domains by IP from file "ipList.txt", output to file "sites.txt"
          2.Port scan those IPs
          3.Get Websites' ICP and check it right
--------------------------------------------
"""
from urllib import request
import re

#Parameter: url is "http://s.tool.chinaz.com/same?=+ip"
#function: Spider url's content, or domain's name, output to "sites.txt"
def getDomains(url):
    response = request.urlopen(url)
    page = response.read()
    page = page.decode('utf-8')
    #print(page)

    var = r'window.open\(\'http://\S+\'\)'
    rr = re.compile(var)
    sites = rr.findall(page)
    #print(sites)

    var2 = "http://[\w+\-*.]+"
    rr2 = re.compile(var2)
    fp = open("sites.txt", "a")
    for st in sites:
        st = rr2.findall(st)
        str = "".join(st)
        print(str)
        fp.write(str+"\n")
    fp.close()

def main():
#url = 'http://s.tool.chinaz.com/same'
#data = input("请输入ip地址： ")
    for data in open("ipList.txt", "rb"):
        url = 'http://s.tool.chinaz.com/same'
        data = str(data, encoding="utf-8")
        url = url+'?s='+ data
        getDomains(url)

if __name__ == '__main__':
    fp = open("sites.txt", "w")
    fp.close()
    main()