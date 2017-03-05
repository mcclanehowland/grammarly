from pyvirtualdisplay import Display
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from random import randint
import time

##Uncomment fo run without opening chrome window
# display = Display(visible=0,size=(800,600))
# display.start()

grammarly_install_link = "https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen"
referral_link = "http://gram.ly/zpWz"
number_of_weeks = 50

##load the grammarly extension
chrome_options = Options()
chrome_options.add_extension('Grammarly-for-Chrome_v14.746.740.crx') #grammarly crx file should be placed in the same folder as this script

driver = webdriver.Chrome(chrome_options=chrome_options) #note that the extensions are loaded via the chrome_options

number_of_weeks_added = 0

for i in range(number_of_weeks):
    try:
        ##navigate to the referral link specified
        driver.get(referral_link)

        #click through to the signup page
        get_grammarly_link = driver.find_element_by_class_name("_555fb3-mainText")
        get_grammarly_link.click()

        #find the text boxes and send letters for login/username/password
        name_box = driver.find_element_by_xpath("//*[@type='name']")
        name_box.send_keys("Holden Caulfield")

        randemail = str(randint(10000,99999))+"@gmail.com"
        email_box = driver.find_element_by_xpath("//*[@type='email']")
        email_box.send_keys(randemail)

        password_box = driver.find_element_by_xpath("//*[@type='password']")
        password_box.send_keys("HuntingHat")
        #fill in the dropdown menu and submit the form
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB,Keys.DOWN,Keys.TAB,Keys.RETURN)
        actions.perform()
        #delay to let page load
        time.sleep(2)
        #exit out of welcome menu
        actions.send_keys(Keys.ESCAPE)
        actions.perform()
        #logout
        logout_button = driver.find_element_by_xpath("//*[contains(text(),'Log out')]")
        logout_button.click()

        driver.delete_all_cookies()
        number_of_weeks_added = number_of_weeks_added+1
        print(number_of_weeks_added)
    except selenium.common.exceptions.NoSuchElementException:
        print("failed: selenium.common.exceptions.NoSuchElementException")
