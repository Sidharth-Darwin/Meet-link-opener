# import pyautogui
# import time

# time.sleep(10)
# # currentMouseX, currentMouseY = pyautogui.position()
# # print(currentMouseX,"and ",currentMouseY)
# i=0
# with open("C:\\Users\\SIDDU\\OneDrive\\Desktop\\work\\.vscode\\spam.txt",encoding='utf8') as f:
#     text=f.readlines()
#     while (i<10):
#         pyautogui.click(1000, 969)
#         pyautogui.write(text[i], interval=0)
#         pyautogui.press('enter')
#         i=i+1


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

# S2R1 Engg Physics

## The following doesnt work because selenium made site wont support logging in with gmail account
# def access_meet(list[-1],options):
#     driver2 = webdriver.Chrome(executable_path=r"C:\\Program Files (x86)\\chromedriver.exe",chrome_options=options)
#     url2 = 'https://meet.google.com/'+str(list[-1].group())
#     driver2.get(url2)
#     time.sleep(5)
#     search2=driver2.find_element_by_id('__lottie_element_2')
#     search2.click()
#     # driver2.quit()
#     time.sleep(5)