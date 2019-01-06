# This will work using headless Chrome for any Desktop OS (Windows, MacOS, Linux Desktop)
from selenium import webdriver
import platform
import time

# Gets the path to the right chromedriver
path = "./chromedriver_2.45/chromedriver_" + platform.system()

links = ['dev.to']

options = webdriver.ChromeOptions()
options.add_argument("headless")


# must install linux browser `sudo apt-get install -y chromium-browser` in Linux
if(platform.system() == 'Linux'):
    options.binary_location = '/usr/bin/chromium-browser'

options.add_argument("disable-infobars")  # disabling infobars
options.add_argument("--disable-extensions")  # disabling extensions
options.add_argument("--disable-gpu")  # applicable to windows os only
# overcome limited resource problems
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")  # Bypass OS security model
# Thanks to https://stackoverflow.com/a/50642913/2291648 for explaining the arguments above

with webdriver.Chrome(path, chrome_options=options) as driver:
    # these values represent the sizes of the entire browser window and not the viewport.
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
        linkWithProtocol = 'http://' + str(link)

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
