from selenium import webdriver
import time
import os
import sys


driverfile_path = r'D:/chromedriver.exe'
driver = webdriver.Chrome(driverfile_path)
driver.get('https://www.e-stat.go.jp/regional-statistics/ssdsview/municipality')
time.sleep(5)
driver.find_element_by_css_selector('#prefectures').click()
time.sleep(5)
for i in range(2, 49):
    driver.find_element_by_css_selector('#prefectures > option:nth-child('+str(i)+')').click()
    name = driver.find_element_by_css_selector('#prefectures > option:nth-child('+str(i)+')').text
    print('================================================================')
    print("第"+str(i)+"县的数据")
    print('================================================================')
    time.sleep(5)
    datas = driver.find_elements_by_css_selector('#stat-area-selector-select-box-prefecture-from > option')
    with open(r"C:\Users\PC\Desktop\日本数据\\"+name+".txt", "w", encoding='UTF-8') as f:
        for data in datas:
            if i == 15 or i == 31 or i == 47:
                a = str(data.text)
                b = a.lstrip()
                c = b[11:]
                print(c)
                f.write(c)
            else:
                a = str(data.text)
                b = a.lstrip()
                c = b[10:]
                print(c)
                f.write(c)
    f.close()
    lines = open(r"C:\Users\PC\Desktop\日本数据\\"+name+".txt", encoding='UTF-8').readlines()
    print(lines)
    fp = open(r"C:\Users\PC\Desktop\日本数据\\"+name+".txt", 'w', encoding='UTF-8')
    for s in lines:
        fp.write(s.lstrip())
    fp.close()
    print('ok')
