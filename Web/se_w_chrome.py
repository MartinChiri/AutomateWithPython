from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd


# options = Options()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])  # ERROR:device_event_log_impl.cc
# options.add_experimental_option('detach', True)

website =  "https://www.thesun.co.uk/sport/football/"

# driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome(options=options, service=Service('chromedriver.exe'))
driver = webdriver.Chrome(service=Service('chromedriver.exe'))
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
df_headlines.to_csv('headline.csv')

driver.quit()



