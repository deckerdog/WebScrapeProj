from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pickle


csv_file = open('camp_test.csv', 'w', newline = '', encoding='utf-8')
writer = csv.writer(csv_file)
headers = ['title','description', '# donations', 'total collected', 'goal', 'date created', 'shares', 'location','category']
writer.writerow(headers)

driver = webdriver.Chrome(r'C:\Users\phili\Desktop\chromedrive\chromedriver.exe')
driver.get("https://www.gofundme.com/discover")

cats = driver.find_elements_by_xpath('//div[@aria-label="GoFundMe categories"]//a')
tos = []
for cat in cats:
    section = cat.get_attribute('href')
    if section is None:
        continue
    else:
        tos.append(section)

adds=[]
for i in tos:
    driver.get(i)
    index = 0
    while index<=0:
        try:
            print("Scraping Section " + str(index))
            y = 12*index
            
            camps = driver.find_elements_by_xpath('//div[@class="cell grid-item small-6 medium-4 js-fund-tile"]')[y:]
            print('='*50)
            index = index + 1
            
            
            for camp in camps:
                
            
                title = camp.find_element_by_xpath('.//div[@class="react-campaign-tile"]/a').get_attribute('href')
                
                
                adds.append(title)
                

            wait_button = WebDriverWait(driver,10)
            next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="button hollow expanded-mobile js-load-more-results"]')))
            next_button.click()
            time.sleep(2)

        except Exception as e:
            print(e)
            break



with open('pages.pkl', 'wb') as f:
    pickle.dump(adds, f)
    f.close()