from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome()
browser.get(START_URL)

brown_dwarf_data = []

def scrape(hyperlink):
    
    page = requests.get(hyperlink)

    soup = BeautifulSoup(page.content, "html.parser")

    data_list = []

    information_to_extract = ["Brown Dwarf: ", "Constellation: ", "Right Ascension: ",
                              "Declination: ", "App Mag: ", "Distance: ", "Spectral type: ",
                              "Mass: ", "Radius: ", "Discovery Year: "]
    
    for info_name in information_to_extract:
                try:
                    value= soup.find('div', text=info_name).find_next('span').text.strip()
                    print(value)
                    data_list.append(value)
                    
                except:
                    data_list.append('Unknown')

    brown_dwarf_data.append(data_list)

headers = ["brown_dwarf","constellation", "right_ascension", "declination", "app_mag", "distance", "spectral_type","mass","radius","discovery_year"]
new_planet_df_1 = pd.DataFrame(brown_dwarf_data,columns = headers)
new_planet_df_1.to_csv('dwarf_stars.csv',index=True, index_label="id")  
    

    