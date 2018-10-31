from selenium import webdriver
import time

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome(r'C:\Users\phili\Desktop\chromedrive\chromedriver.exe')
# Go to the page that we want to scrape
driver.get("https://www.gofundme.com/discover/medical-fundraiser")

# Click review button to go to the review section
#review_button = driver.find_element_by_xpath('//span[@class="padLeft6 cursorPointer"]')
#review_button.click()

# Page index used to keep track of where we are.
index = 1
# We want to start the first two pages.
# If everything works, we will change it to while True
while index <=1:
	try:
		print("Scraping Section " + str(index))
		index = index + 1
		# Find all the reviews. The find_elements function will return a list of selenium select elements.
		# Check the documentation here: http://selenium-python.readthedocs.io/locating-elements.html
		camps = driver.find_elements_by_xpath('//div[@class="cell grid-item small-6 medium-4 js-fund-tile"]')
		print(len(camps))
		print('='*50)
		# Iterate through the list and find the details of each review.
		for camp in camps:
			# Initialize an empty dictionary for each review
			camp_dict = {}
			# Use relative xpath to locate the title, content, username, date, rating.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use `element.get_attribute()`
			title = camp.find_element_by_xpath('.//div[@class="fund-title truncate-single-line show-for-medium"]').text
			# Your code here
			fund_text = camp.find_element_by_xpath('.//div[@class="fund-item fund-description clamp mb"]').text
			fund_prog = camp.find_element_by_xpath('.//div[@class="show-for-medium"]').text
			print(title)
			print(fund_text)
			print(fund_prog)
			print('*'*50)

			#review text


		# Locate the next button element on the page and then call `button.click()` to click it.
		#wait_button = WebDriverWait(driver,10)
		#next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//a[@class="button hollow expanded-mobile js-load-more-results"]'))
		#next_button.click()
		#time.sleep(2)

	except Exception as e:
		print(e)
		driver.close()
		break
