# This will work for any Desktop OS (Windows, MacOS, Linux Desktop)
from selenium import webdriver
import platform
import time

path = "./chromedriver_2.45/chromedriver_" + platform.system()

links = ['dev.to']

with webdriver.Chrome(path) as driver:
    for link in links:
        desktop = {'output': str(link) + '-desktop.png',
                   'width': 2200,
                   'height': 1800}
        tablet = {'output': str(link) + '-tablet.png',
                  'width': 1200,
                  'height': 1400}
        mobile = {'output': str(link) + '-mobile.png',
                  'width': 680,
                  'height': 1200}
        linkWithProtocol = 'https://' + str(link)

        # set the window size for desktop
        driver.set_window_size(desktop['width'], desktop['height'])
        driver.get(linkWithProtocol)
        time.sleep(2)
        driver.save_screenshot(desktop['output'])

        # set the window size for tablet
        driver.set_window_size(tablet['width'], tablet['height'])
        driver.get(linkWithProtocol)
        time.sleep(2)
        driver.save_screenshot(tablet['output'])

        # set the window size for mobile
        driver.set_window_size(mobile['width'], mobile['height'])
        driver.get(linkWithProtocol)
        time.sleep(2)
        driver.save_screenshot(mobile['output'])
