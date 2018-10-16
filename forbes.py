#import selenium package
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import csv
import re

#creating driver
driver = webdriver.Chrome(r'C:\Users\patel\OneDrive\Desktop\chromedriver.exe')
driver.get("https://www.forbes.com/billionaires/list/50/#version:static")

#open 'reviews.csv' file in write mode
csv_file = open('reviews.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)

#finding values for Rank, Name and Net_Worth by xpath
Rank = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]/td[@class = "rank"]')))
Name =list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]/td[@class = "name"]')))
Net_Worth = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]/td[@class = "networth"]')))
wait_button = WebDriverWait(driver, 10)# wait

#finding values for Age, Source and Country of citizenship by xpath
Age = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]//td[5]')))
Source = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]//td[6]')))
Country = list(map(lambda x: x.text, driver.find_elements_by_xpath('//tbody/*[@class="data"]//td[7]')))
wait_button = WebDriverWait(driver, 10)#wait

# filter data with the help of regular expression
Rank = [(re.sub('[\n,. - #]+',"", i)) for i in Rank]
Name = [(re.sub('[\n,.-]+',"", i)) for i in Name]
Net_Worth = [(re.sub('[\n, - # B $]+',"", i)) for i in Net_Worth]
Age = [(re.sub('[\n,.-]', '', i)) for i in Age]
Source = [(re.sub('[\n,.-]', '', i)) for i in Source]
Country = [(re.sub('[\n,.-]', '', i)) for i in Country]

#combine values by using zip function
data_dict = zip(Rank, Name, Net_Worth, Age, Source, Country)

#writing data_dict into csv file
writer.writerows(data_dict)

#closing csv file
csv_file.close()

#closing driver
driver.close()