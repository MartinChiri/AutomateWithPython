from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
#driver_path = '/usr/local/bin/operadriver'
#driver_path = '/home/martinchiri/Documents/AutomateWithPython/Web/chromedriver_linux64'
brave_path = '/usr/bin/brave-browser'

options.binary_location = brave_path
options.add_argument('--remote-debugging-port=9224') #NOT 9222

#drvr = webdriver.Chrome(options=options, executable_path=driver_path)
drvr = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
drvr.get('https://stackoverflow.com')
drvr.quit


