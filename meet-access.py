
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import webbrowser

full_user_name = input("Enter the name of the individual/group: ")

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"C:\\Program Files (x86)\\chromedriver.exe",chrome_options=options)

url1 = 'https://web.whatsapp.com'
driver.get(url1)
time.sleep(20)

search= driver.find_element_by_css_selector(f'span[title="{full_user_name}"]')
search.click()
list=[]
tex_list= driver.find_elements_by_css_selector('span[class="i0jNr selectable-text copyable-text"]')
for tex in tex_list:
    text=tex.text
    match = re.search('[a-z]{3}\-[a-z]{4}\-[a-z]{3}',text)
    if match:
        list.append(match)

url2 = 'https://meet.google.com/'+str(list[-1].group())
webbrowser.open(url2)
time.sleep(5)

driver.quit()

