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
with open(r"C:\Users\PC\Desktop\县.txt", "w", encoding="UTF-8") as f:
    for i in range(2, 49):
        county = driver.find_element_by_css_selector("#prefectures > option:nth-child("+str(i)+")").text
        print("第一个"+str(i-1)+"县，爬取成功")
        print(county)
        f.write(county)
        f.write('\n')
f.close()




# from selenium import webdriver
# import time
# import os
# import sys
# import pymysql
# print("连接mysql数据库")
# db = pymysql.connect(host='localhost', user='root', password='mysql密码', port=3306, db='AREA')
# print("mysql连接成功")
# cursor = db.cursor()
# sql = """CREATE TABLE  area (
#         id int not null auto_increment PRIMARY KEY,
#         area CHAR(10) not null )"""
# cursor.execute(sql)
#
# driverfile_path = r'D:/chromedriver.exe'
# driver = webdriver.Chrome(driverfile_path)
# driver.get('https://www.e-stat.go.jp/regional-statistics/ssdsview/municipality')
# time.sleep(5)
# driver.find_element_by_css_selector('#prefectures').click()
# time.sleep(5)
# for i in range(2, 49):
#     county = driver.find_element_by_css_selector("#prefectures > option:nth-child(" + str(i) + ")").text
#     print("第一个" + str(i - 1) + "县，爬取成功")
#     print(county)
#     insert_area = ("INSERT INTO area(area)" "VALUES(%s)")
#     print(county)
#     try:
#         cursor.execute(insert_area, county)
#         db.commit()
#     except:
#         print("插入失败")
#         db.rollback()
# print("爬取数据完毕，并插入了mysql中")





