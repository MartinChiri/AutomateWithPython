from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach', True)
drvr = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
drvr.get('https://stackoverflow.com')



