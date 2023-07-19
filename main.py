from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://tinder.com/")
driver.maximize_window()

email = "yzjccy123456@gmail.com"
passwords = "Ccyyzj230109"

time.sleep(10)

log_in_button = driver.find_element(By.XPATH,
									'//*[@id="t1951895747"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()

time.sleep(10)

accpet_button = driver.find_element(By.XPATH, '//*[@id="t223514671"]/main/div[2]/div/div/div[1]/div[1]/button')
accpet_button.click()

time.sleep(10)

log_with_facebook = driver.find_element(By.XPATH,
										'//*[@id="t223514671"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
log_with_facebook.click()

time.sleep(10)

driver.maximize_window()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(10)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(15)

username = driver.find_element(By.ID, 'email')
username.send_keys(email)
password = driver.find_element(By.ID, 'pass')
password.send_keys(passwords)

time.sleep(10)

log_in = driver.find_element(By.ID, 'loginbutton')
log_in.click()

time.sleep(10)

driver.switch_to.window(base_window)
print(driver.title)

# Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="t223514671"]/main/div/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(10)

# Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="t223514671"]/main/div/div/div/div[3]/button[1]')
notifications_button.click()

time.sleep(10)

# Allow cookies
cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')
cookies.click()

time.sleep(10)

for n in range(5):

	time.sleep(5)

	try:
		print("called")
		like_button = driver.find_element(By.XPATH,
										  '//*[@id="t1951895747"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
		like_button.click()

	except ElementClickInterceptedException:
		try:
			match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
			match_popup.click()


		except NoSuchElementException:
			time.sleep(5)

driver.quit()
