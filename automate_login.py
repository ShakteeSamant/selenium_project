from selenium import webdriver
username = ''
password = ''

url = 'http://hrms.turabit.com/symfony/web/index.php/auth/login'
page = "http://hrms.turabit.com/symfony/web/index.php/attendance/punchOut"
browser = webdriver.Chrome(executable_path =r"C:\driver\chromedriver.exe")
browser.get(url)


username_entry = browser.find_element_by_id("txtUsername")
username_entry.send_keys(username)

password_entry = browser.find_element_by_id("txtPassword")
password_entry.send_keys(password)

login = browser.find_element_by_id("btnLogin")
login.click()

browser.get(page)

punch = browser.find_element_by_id("btnPunch")
punch.click()

browser.close()
