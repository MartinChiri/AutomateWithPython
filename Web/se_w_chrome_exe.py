from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import sys

# Preparing script before we convert it to executable
application_path = os.path.dirname(sys.executable)

# get date in format MMDDYYYY
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")


options = Options()
options.headless = True

website =  "https://www.thesun.co.uk/sport/football/"


driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(website)
# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/h3').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'football_headlines_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()

#  pyinstaller --onefile se_w_chrome_exe.py



