# This is the full program to access whatsapp using selenium and open meet link using webbrowser modules in python.

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import webbrowser

# Here the user is suppose to enter the name of the person/group chat from where to access link.
# For easy access just put a default name as string.
full_user_name = input("Enter the name of the individual/group: ")

# Creating a web driver using selenium.
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"C:\\Program Files (x86)\\chromedriver.exe",chrome_options=options)

# Accessing the whatsapp web link using the created driver.
url1 = 'https://web.whatsapp.com'
driver.get(url1)

# There is a time delay given for the user to login in into whatsapp.web using QR code.
# Unfortunately this makes the whole program semi automatic cause its a necessasary step.
time.sleep(20)

# To store all the available meet links in last 13 messages of the chat.
# Only final entry will be used.
list=[]

# Reading all the messages and filtering out the meet links using Regex.
search= driver.find_element_by_css_selector(f'span[title="{full_user_name}"]')
search.click()
tex_list= driver.find_elements_by_css_selector('span[class="i0jNr selectable-text copyable-text"]')
for tex in tex_list:
    text=tex.text
    match = re.search('[a-z]{3}\-[a-z]{4}\-[a-z]{3}',text) 
    if match:
        list.append(match)

# Since selenium creats a seprate safe browser rather than opening ordinary browser, logging in with email for joining meet is impossible in a way.
# So I used another webbrowser module to open the last found meet link from the specified person/group chat.
url2 = 'https://meet.google.com/'+str(list[-1].group())
webbrowser.open(url2)
time.sleep(5)

# Closing the driver created before.
driver.quit()


