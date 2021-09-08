from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

EXTENSION_PATH = r'./10.0.2_0.crx'

EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

# EXTENSION_PATH = r'10.0.2_0.crx'
def launchSeleniumWebdriver(driverPath):

    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)
    time.sleep(5)
    print("Extension has been loaded")
    return driver

def metamaskSetup(recoveryPhrase, password):

    driver.switch_to.window(driver.window_handles[0])

    driver.find_element_by_xpath('//button[text()="Get Started"]').click()
    driver.find_element_by_xpath('//button[text()="Import wallet"]').click()
    driver.find_element_by_xpath('//button[text()="No Thanks"]').click()

    time.sleep(5)

    inputs = driver.find_elements_by_xpath('//input')
    inputs[0].send_keys(recoveryPhrase)
    inputs[1].send_keys(password)
    inputs[2].send_keys(password)
    driver.find_element_by_css_selector('.first-time-flow__terms').click()
    driver.find_element_by_xpath('//button[text()="Import"]').click()

    time.sleep(5)

    driver.find_element_by_xpath('//button[text()="All Done"]').click()
    time.sleep(2)

    # closing the message popup after all done metamask screen
    driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
    time.sleep(2)
    print("Wallet has been imported successfully")
    time.sleep(10)


def changeMetamaskNetwork(networkName):
    launchSeleniumWebdriver('C:\Drivers\chromedriver_win32\chromedriver.exe')
    metamaskSetup('vast subject prize relax valid section shell jealous fun army pear boring', 'metamask123')
    # opening network
    print("Changing network")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('chrome-extension://{}/home.html'.format(EXTENSION_ID))
    print("closing popup")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()

    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span').click()
    time.sleep(2)
    print("opening network dropdown")
    elem = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div')
    time.sleep(2)
    all_li = elem.find_elements_by_tag_name("li")
    time.sleep(2)
    for li in all_li:
        text = li.text
        if(text == networkName):
            li.click()
            print(text, "is selected")
            time.sleep(2)
            return
    time.sleep(2)
    print("Please provide a valid network name")

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

def connectToWebsite():

    time.sleep(3)

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    time.sleep(3)
    print('Site connected to metamask')
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

def confirmApprovalFromMetamask():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(10)
    # confirm approval from metamask
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]').click()
    time.sleep(12)
    print("Approval transaction confirmed")

    # switch to dafi
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)


def rejectApprovalFromMetamask():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(10)
    # confirm approval from metamask
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[1]').click()
    time.sleep(8)
    print("Approval transaction rejected")

    # switch to dafi
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    print("Reject approval from metamask")


def confirmTransactionFromMetamask():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(10)

    # # confirm transaction from metamask
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]').click()
    time.sleep(13)
    print("Transaction confirmed")

    # switch to dafi
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(3)


def rejectTransactionFromMetamask():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(5)
    # confirm approval from metamask
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[1]').click()
    time.sleep(2)
    print("Transaction rejected")

    # switch to dafi
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
