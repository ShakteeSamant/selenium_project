import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

username = ''
password = ''

url = 'http://hrms.turabit.com/symfony/web/index.php/auth/login'
# driver = webdriver.Chrome(executable_path ="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
# driver.get(url)
#
# from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import time

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome(executable_path ="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
driver.get(url)

