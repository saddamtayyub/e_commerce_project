from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager  # chrome

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.justdial.com/')

# Checking the name of website
assert 'Justdial' in driver.title
print(driver.title)

# for entering city and selecting it
city = "goa"
city_input = driver.find_element_by_css_selector('input#city')
city_input.click()
city_input.send_keys(city)
driver.implicitly_wait(0.4)
select_city_option = driver.find_element_by_css_selector('#{}'.format(city.capitalize()))
print(select_city_option.text, "before click")
driver.implicitly_wait(4)
select_city_option.click()
print(select_city_option.text, "after click")

# for entering input into search box
text_to_search = "car repair"
search_box = driver.find_element_by_id('srchbx')
search_box.clear()
search_box.send_keys('{}'.format(text_to_search))
search_box.send_keys(Keys.RETURN)

# print(driver.current_url)
# driver.close()
