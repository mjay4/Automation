from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')

reg = browser.find_element_by_css_selector('#email')

pas = browser.find_element_by_css_selector('#pass')

reg.send_keys('your_user_name')
pas.send_keys('your_actual_password')

submit = browser.find_element_by_css_selector('#u_0_b')
submit.click()
