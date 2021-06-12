import requests
from selenium import webdriver
import time
from tqdm import tqdm
import csv
from openpyxl import Workbook

browser = webdriver.Chrome()


#from tqdm import tqdm
reviewData = list()
# links = browser.find_element_by_class_name('paging').find_elements_by_tag_name('a')
#_iter = 1000
#for page in tqdm(range(_iter)):
for page in range(11):
    url = 'https://www.mangoplate.com/search/경기도-디저트?keyword=경기도%20디저트&page='+str(page)
    browser.get(url)
    print(url)
    browser.implicitly_wait(10)  # 각 요소를 10초를 기다린 후 scrap한다
    for row in browser.find_elements_by_tag_name('img'):
        total = row.get_attribute('alt').split('-')
        cafe_name = total[0].split(' ')[0]
        if len(total)<2 or total[1].isalpha():
            continue
        cafe_addr = total[1]
        reviewData.append((cafe_name,cafe_addr))
        print("cafe_name",cafe_name)
        print("cafe_addr",cafe_addr)
    #browser.find_element_by_class_name('PaginationTypeNextPrev__Button PaginationTypeNextPrev__NextButton PaginationTypeNextPrev__NextButton--Active').click()

csvFile = open("./reviewData.csv","a",encoding='utf-8',newline="\n") #파일오픈
csvWriter = csv.writer(csvFile)

for row in reviewData:
    csvWriter.writerow(row)

csvFile.close()