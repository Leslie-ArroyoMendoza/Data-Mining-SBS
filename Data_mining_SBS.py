#############################################################
# Library importation #######################################
#############################################################
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd
##############################################################
# DRIVER #####################################################
##############################################################
# indicate the path where the driver is located
s=Service(r'C:\Users\lesli\Documents\geckodriver.exe')
##############################################################
# Load the the driver ########################################
browser=webdriver.Firefox(service=s)
url1="https://www.sbs.gob.pe/app/stats_net/stats/EstadisticaBoletinEstadistico.aspx?p=1#"
##############################################################
# Open the url inside the driver 
##############################################################
browser.get(url1)
browser.implicitly_wait(30)

##############################################################
# Find the xpath of the elements to click
##############################################################
# 1. Click on menu
# 2. Click on submenu
# 3. 

step1="/html/body/form/table[3]/tbody/tr/td/table/tbody/tr/td[1]/div/div/div/div/div[8]/div/a"
step2="/html/body/form/table[3]/tbody/tr/td/table/tbody/tr/td[1]/div/div/div/div/div[9]/div/div/a"
step3="//*[@id='ImgFlecha']"
###############################################################
# Follow the steps inside the driver ##########################
###############################################################
WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH, step1))).click()
WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH, step2))).click()
WebDriverWait(browser,30).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'output')))
# Move to the bottom of the page ##############################
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH, step3))).click()

# Create a list to keep the urls ##############################
links=[]
# Find all html elements starting with tag name 'a'
find_urls=WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.TAG_NAME,'a')))
# extract the link from all the elements saved in the "find_urls" list
for x in find_urls:
    link=x.get_attribute('href')
    # select links that came after 2008
    year=re.search('financiera/(.+?)/',link).group(1)
    if int(year) > 2008 :
        links.append(link)
# Close the driver
browser.close()

# Save the data frame with all the links
df=pd.DataFrame(links)
df.to_csv(r"C:\Users\lesli\Documents\MEGAsync\Observatorio\Boitano\lista_links_excels.csv", index=False)

