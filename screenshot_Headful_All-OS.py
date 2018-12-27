from selenium import webdriver
import time

links = ['dev.to']

with webdriver.Chrome("C:/chromedriver_win32/chromedriver") as driver:
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
