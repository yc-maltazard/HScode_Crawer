#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
Title = HSCode.net Spyder
Date = 2018-4-11
Author = Maltazard
'''

import requests, re, csv, sys, io

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8') #改变标准输出的默认编码

with open("test.csv", "w", newline='',encoding='gb18030') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["HS编码", "商品名称", "商品规格"])
    csvfile.close()

hscode_file = open('hscode.txt',encoding='UTF-8')
line = hscode_file.readline()
#print(line)

for line in hscode_file:
    hscode = line.strip()
    #print(hscode)
    url = 'https://www.365area.com/hscode/detail/'+ hscode
    print(url)
    content = requests.get(url).text
    #print(content)
    #pattern = re.compile('<div.*?"even".*?<b>\s(\d+.\d+)</b>.*?</div>.*?<div.*?"even">.*?(\w+)</div>',re.S)
    #pattern = re.compile('<div\sid="sbsl">.*?<tr>.*?(\d+.\d+)</td>.*?<td>(\w+)</td>.*?<td\s>(\w+)</td>',re.S)
    pattern = re.compile('<tr>.*?<td.*?ali.*?>.*?(\d+.\d+)</td>.*?<td>(.*?)</td>.*?<td\s>(.*?)</td>',re.S)
    results = re.findall(pattern,content)
    #print(results)
    if results == "":
        break
    else:
        with open("test.csv", "a", newline='',encoding='gb18030') as csvfile:
            writer = csv.writer(csvfile)
            for result in results:
                hscodewithdot = str(result[0])
                data = [hscodewithdot,result[1],result[2]]
                print(data)
                #print(result[0])
                writer.writerow(data)
            csvfile.close()
hscode_file.close()