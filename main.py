
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{
    "download.default_directory" : "D:\Diego\Documents\TESIS\Images",
})

def download_insta(link):
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chromeOptions)
    driver.get("https://downloadgram.org/")
    text_box = driver.find_element("name", "url")
    text_box.send_keys(link)

    driver.find_element(By.ID, value='submit').click()
    time.sleep(1)
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
    #print(link)
    download_insta(link)
