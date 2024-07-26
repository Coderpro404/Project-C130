from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import requests

# URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(2)

scraped_data = []

def scrape():
    for i in range(0, 5):  # Looping through a range of 10 pages (adjust as needed)
        print(f'Scraping page {i+1} ...')

        soup = BeautifulSoup(browser.page.page_source, "html.parser")

        bright_star_table = soup.find("table", attrs={"class","wikitable"})
        
        table_body = bright_star_table.find('tbody')

        table_rows = table_body.find_all('tr')

        for row in table_rows:
            table_cols = row.find_all('td')
            print(table_cols)

            temp_list = []

            for col_data in table_cols:
                print(col_data.text)
                
                data = col_data.text.strip()
                temp_list.append(data)

            scraped_data.append(temp_list)

    stars_data = []

    for i in range(0,len(scraped_data)):
        Star_names = scraped_data[i][1]
        Distance = scraped_data[i][3]
        Mass = scraped_data[i][5]
        Radius = scraped_data[i][6]
        Lum = scraped_data[i][7]
        required_data = [Star_names, Distance, Mass, Radius, Lum] 
        stars_data.append(required_data)                

    headers = ['Star_name','Distance','Mass','Radius','Luminosity']

    star_df_1 = pd.DataFrame(stars_data, columns = headers)
    star_df_1.to_csv('bright_stars.csv',index = True, index_label = "id")