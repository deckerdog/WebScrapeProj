from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


csv_file = open('camp_test.csv', 'w', newline = '', encoding='utf-8')
writer = csv.writer(csv_file)
headers = ['title','description', '# donations', 'total collected', 'goal', 'date created', 'shares', 'donations']
writer.writerow(headers)

driver = webdriver.Chrome(r'C:\Users\phili\Desktop\chromedrive\chromedriver.exe')
driver.get("https://www.gofundme.com/discover/medical-fundraiser")


index = 0
adds=[]
while index <=0:
	try:
		print("Scraping Section " + str(index))
		y = 12*index
		
		camps = driver.find_elements_by_xpath('//div[@class="cell grid-item small-6 medium-4 js-fund-tile"]')[y:]
		print('='*50)
		index = index + 1
		
		
		for camp in camps:
			
		
			title = camp.find_element_by_xpath('.//div[@class="react-campaign-tile"]/a').get_attribute('href')
			
			
			adds.append(title)
			


		print(len(adds))
		wait_button = WebDriverWait(driver,10)
		next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="button hollow expanded-mobile js-load-more-results"]')))
		next_button.click()
		time.sleep(2)

	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break


for add in adds:
    campaign_dict = {}

    driver.get(add)
    title = driver.find_element_by_xpath('//h1[@class="campaign-title"]').text
    desc = driver.find_element_by_xpath('//*[@id="story"]/div[3]').text
    by = driver.find_element_by_xpath('//*[@id="js-side-column"]/div[2]/div[2]').text
    total = driver.find_element_by_xpath('//*[@id="js-side-column"]/div[2]/h2/strong').text
    goal = driver.find_element_by_xpath('//*[@id="js-side-column"]/div[2]/h2/span').text
    created = driver.find_element_by_xpath('//*[@id="js-side-column"]/div[3]/div[1]/div[1]').text
    shares = driver.find_element_by_xpath('//strong[@class="js-share-count-text"]').text
    #location = driver.find_element_by_xpath('//*[@id="js-side-column"]/div[3]/div[2]/div/div[2]/a[2]').text
    #medical = driver.find_element_by_xpath('//*[@id="js-side-column"]/div[3]/div[2]/div/div[1]').text

    wait_button = WebDriverWait(driver,10)
    next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="button secondary expanded hide-in-modal"]')))
    next_button.click()
    time.sleep(2)

    dons = []
    cons = driver.find_elements_by_xpath('//div[@class="supporter js-donation-content "]')
    for con in cons:
        x = con.find_element_by_xpath('.//div[@class="supporter-amount"]').text
        dons.append(x)

    
    
    #campaign_dict['title'] = titles
    #campaign_dict['description'] = desc
    #campaign_dict['# donations'] = by
    ##campaign_dict['total collected'] = total
    #campaign_dict['goal'] = goal
    #campaign_dict['Date created'] = created
    #campaign_dict['shares'] = shares
    #campaign_dict['location'] = location
    #campaign_dict['type'] = medical
    #campaign_dict['donations'] = don
    #writer.writerow(campaign_dict.values())
    print(len(dons))
    

