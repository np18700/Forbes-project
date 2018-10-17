#import selenium package
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import csv
import re

driver = webdriver.Chrome(r'C:\Users\patel\OneDrive\Desktop\chromedriver.exe')
driver.get("https://www.forbes.com/billionaires/list/50/#version:static_tab:women")

csv_file = open('reviews.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)

Rank = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]/td[@class = "rank"]')))
Name =list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]/td[@class = "name"]')))
Net_Worth = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]/td[@class = "networth"]')))
wait_button = WebDriverWait(driver, 10)


Age = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]//td[5]')))
Source = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]//td[6]')))
Country = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]//td[7]')))
wait_button = WebDriverWait(driver, 10)

Rank = [(re.sub('[\n , . - #]+',"", i)) for i in Rank]
Name = [(re.sub('[\n,.-]+',"", i)) for i in Name]
Net_Worth = [(re.sub('[\n , - # B $]+',"", i)) for i in Net_Worth]
Age = [(re.sub('[\n,.-]', '', i)) for i in Age]
Source = [(re.sub('[\n,.-]', '', i)) for i in Source]
Country = [(re.sub('[\n,.-]', '', i)) for i in Country]

data_dict = zip(Rank, Name, Net_Worth, Age, Source, Country)

writer.writerows(data_dict)
csv_file.close()
driver.close()