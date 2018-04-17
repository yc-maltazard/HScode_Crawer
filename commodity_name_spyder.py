#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Title = commodity_name_spyder
Date = 2018-4-16'''
#__author__ = Maltazard

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests, re, csv, sys, io, datetime

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8') #改变标准输出的默认编码

with open("test.csv", "w", newline='',encoding='gb18030') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["HScode", "商品名称"])
    csvfile.close()
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
headers = {'User-Agent': User_Agent}

hscode_file = open('hscode.txt',encoding='UTF-8')
line = hscode_file.readline()
#print(line)
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'X:\Python34\Scripts\chromedriver.exe')

for line in hscode_file:
    hscode = line.strip()
    #print(hscode)
    url = 'http://www.hs-bianma.com/search.php?ser=' + hscode +'&flag=1'
    print(url)

    #def LoadPageContent(self,page):
        #记录开始时间
    #    begin_time = datetime.datetime.now()
    driver.get(url)
    content = driver.page_source
    #content = requests.get(url).text
    #print(content)
    #pattern = re.compile('<div.*?"even".*?<b>\s(\d+.\d+)</b>.*?</div>.*?<div.*?"even">.*?(\w+)</div>',re.S)
    #pattern = re.compile('<div\sid="sbsl">.*?<tr>.*?(\d+.\d+)</td>.*?<td>(\w+)</td>.*?<td\s>(\w+)</td>',re.S)
    pattern = re.compile('red.*?red.*?>(.*?)</span>(.*?)</span></div><div>(.*?)</div><div><a',re.S)
    #pattern = re.compile('<tr>.*?<td.*?ali.*?>.*?(\d+.\d+)</td>.*?<td>(.*?)</td>.*?<td\s>(.*?)</td>',re.S)
    results = re.findall(pattern,content)
    print(results)
    if results == "":
        break
    else:
        with open("test.csv", "a", newline='',encoding='gb18030') as csvfile:
            writer = csv.writer(csvfile)
            for result in results:
                hscodewithdot = str(result[0]) + str(result[1])
                data = [hscodewithdot,result[2]]
                print(data)
                #print(result[0])
                writer.writerow(data)
            csvfile.close()
driver.quit()
hscode_file.close()