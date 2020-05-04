import time
from selenium import webdriver
import pickle
from selenium.webdriver.common.keys import Keys
# from pynput.keyboard import Key, Controller

import pyautogui as pag
# import keyboard



from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/etc/alternatives/google-chrome"    #chrome binary location specified here
options.add_argument("--start-maximized") #open Browser in maximized mode
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)







driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
# driver = webdriver.Firefox()




def loginZoom():
    driver.get('https://us04web.zoom.us/signin')
    time.sleep(2)
    driver.find_element_by_name('email').send_keys('kappaterapappa@gmail.com')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('Majnu123')
    time.sleep(1)
    # driver.find_element_by_link_text('Sign In')
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    time.sleep(3)


    driver.get('https://web.whatsapp.com/')








# time.sleep(10)
def clearMess1():
    try:
        # driver.find_element_by_css_selector('#main > header > div.YmSrp > div > div:nth-child(3)').click()
        # ._3TbsN > div:nth-child(1) > span:nth-child(1)
        element = driver.execute_script('return document.querySelector("#main > header > div.YmSrp > div > div:nth-child(3)")')
        element.click()
        time.sleep(0.4)
        # driver.find_element_by_css_selector('#main > header > div.YmSrp > div > div.rAUz7._3TbsN > span > div > ul > li:nth-child(4) > div').click()
        element = driver.execute_script('return document.querySelector("#main > header > div.YmSrp > div > div.rAUz7._3TbsN > span > div > ul > li:nth-child(4) > div")')

        element.click()
        time.sleep(0.5)
        element = driver.execute_script('return document.querySelector("#app > div > span:nth-child(2) > div > div > div > div > div > div > div._3QNwO > div._1WZqU.PNlAR")')
        element.click()
        # driver.find_element_by_css_selector('#app > div > span:nth-child(2) > div > div > div > div > div > div > div._3QNwO > div._1WZqU.PNlAR').click()
        print('cleared')
    except:
        print('clear not working')




def clearMess():
    try:
        # driver.find_element_by_css_selector('#main > header > div.YmSrp > div > div:nth-child(3)').click()
        # driver.find_e

        element = driver.execute_script('return document.querySelector("#main > header > div.YmSrp > div > div:nth-child(2)")')
        element.click()
        time.sleep(0.4)
        # driver.find_element_by_css_selector('#main > header > div.YmSrp > div > div.rAUz7._3TbsN > span > div > ul > li:nth-child(4) > div').click()
        element = driver.execute_script('return document.querySelector("li._3L0q3:nth-child(4) > div:nth-child(1)")')
        element.click()
        time.sleep(0.5)
        element = driver.execute_script('return document.querySelector("div._1WZqU:nth-child(2)")')
        element.click()
        # driver.find_element_by_css_selector('#app > div > span:nth-child(2) > div > div > div > div > div > div > div._3QNwO > div._1WZqU.PNlAR').click()
        print('cleared')
    except:
        print('clear not working')

def openFirstTime():
    # driver.get('https://web.whatsapp.com/')
    time.sleep(1)
    # whatsapp = driver.window_handles[0]
    try:

        driver.maximize_window()
        time.sleep(15)
        driver.find_element_by_class_name("_3j7s9").click()
        time.sleep(1)
    except:
        print('qr not scanned')



    try:
        # html = driver.execute_script("return document.querySelector('#main > div._3zJZ2 > div > div > div._9tCEa > div.vW7d1.message-in > div > div > div').innerHTML;")
        html = driver.find_element_by_class_name('Tkt2p').get_attribute('innerHTML')
        clearMess()
        return html
    except:
        return False


def checkAgain():
    try:
        try:
            # html = driver.execute_script("return document.querySelector('#main > div._3zJZ2 > div > div > div._9tCEa > div.vW7d1._2Rrsd.message-in.focusable-list-item > div > div.MVjBr._3e2jK > div').innerHTML;")
            # element = driver.find_element_by_css_selector('#main > div._3zJZ2 > div > div > div._9tCEa > div.vW7d1._2Rrsd.message-in.focusable-list-item > div > div.MVjBr._3e2jK > div')
            html = driver.find_element_by_class_name('Tkt2p').get_attribute('innerHTML')
            print(html)
            # return html
            clearMess()
            link = extractLink(html)
            print(link)
            window = openNewTab(link)

            joinClass(link)
            time.sleep(2)
            try:
                pass
                # driver.switch_to_window(window[0])
            except:
                print('no new tab')


            print('joined the class')
        except:
            print('mess have to be cleared')
            clearMess()
            return False

    except:
        # clearMess()
        return 'window error'



def openNewTab(link):
    # clearMess()
    if link == False:
        return False
    else:
        # driver.get('https://web.whatsapp.com/')
        whatsapp = driver.window_handles[0]
        time.sleep(1)
        driver.execute_script('window.open("");')
        time.sleep(1)
        newTab = driver.window_handles[1]
        driver.switch_to_window(newTab)
        time.sleep(3)
        driver.get(link)
        return [whatsapp,newTab]





def extractLink(html):
    if html == False:
        print('no link available')
        return False
        clearMess()
    else:
        try:
            splited = html.split('<a href="')
            splited1 = splited[1].split('"')
            print('          ')
            link = splited1[0]
            return link
        except:
            print('msg has no link')
            return False



def joinClass(link):
    # time.sleep(3)
    # driver.get(link)
    time.sleep(8)
    # obj = driver.switch_to.ale
    pag.press('tab')
    print('got alert')
    time.sleep(2)
    pag.press('enter')
    # elem = driver.find_element_by_tag_name('body')
    if link != False:
        driver.close()
    time.sleep(2)


    # elem.click()
    # elem.send_keys(Keys.CONTROL + 'w')
    time.sleep(3)


    print('closed the tab')

    # driver.execute_script('close()')
    try:
        driver.switch_to.window(driver.window_handles[0])
        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
        # driver.switch_to_window(window[0])
        # driver.send_keys(Keys.CONTROL + 'w')
        # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    except:
        print('some thing is # WARNING: ')







driver.get('https://web.whatsapp.com/')
# loginZoom()
# print('logged in to zoom')
time.sleep(10)
html = openFirstTime()
print('parsed the html',html)
link = extractLink(html)
print('parsing link',link)
window = openNewTab(link)
# driver.switch_to_window(window[0])
joinClass(link)


try:
    driver.switch_to_window(window[0])
except:
    print('no new tab')

# openNewTab('https://www.w3schools.com/jsref/met_win_open.asp')

# print(link)
while True:
    time.sleep(10)
    print(checkAgain())
