# This is a sample Python script.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time



def download_insta(link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://downloadgram.org/")
    text_box = driver.find_element("name", "url")
    text_box.send_keys(link)

    driver.find_element(By.ID, value='submit').click()
    time.sleep(5)
    try:
        driver.find_element(By.LINK_TEXT, value='DOWNLOAD').click()
        time.sleep(1)
        print("Descarga exitosa")
        driver.close()
    except:
        print("page down")
        driver.close()
    return None


links_file = pd.read_csv('LinkTesis.csv')
links = links_file['Links']

for link in links:
    print(link)
    download_insta(link)
