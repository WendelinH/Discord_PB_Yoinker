from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # time.sleep(sekunden) ist "delay"
import sys
import webbrowser

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
discord_Id = sys.argv[1]

url = 'https://discord.id/'

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.set_window_position(50, 50)
driver.set_window_size(800, 600)
driver.implicitly_wait(10) # seconds
driver.get(url)

inputId = driver.find_element_by_id('inputid')
inputId.clear()
inputId.send_keys(discord_Id)

button_lookup = driver.find_element_by_tag_name('button')
button_lookup.click()

button_antiboot = driver.find_element_by_class_name('frc-button')
button_antiboot.click()

discord_PB = driver.find_element_by_class_name('avyimg')
src_PB = discord_PB.get_attribute('src')
print(" ")
print("PB-Element : src")
print(src_PB)

webbrowser.open_new_tab(f"{src_PB}")

driver.close()
