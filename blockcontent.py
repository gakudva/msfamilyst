from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
import sys

def test_blockcontent():

    #Login to family account
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)

    driver.get('https://family.microsoft.com')

    #click on the Login button
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='mectrl_headerPicture']")))
    element.click()

    #enter user name, and ENTER
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#i0116")))
    element.send_keys("user@live.com")   #insert your user here; or do manual input
    sleep(15)                            #wait to support manual input
    element.send_keys(Keys.ENTER)

    #wait for manual input of the 2nd Factor authentication if applicable
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Stay signed in?')]")))

    #Get rid of the pop-up asking to keep the session; he has no clue that he is in a selenium session
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#idBtn_Back")))
    element.click()

    #Select the Family member by name
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//img[@alt='Family member name']"))) # <- replace with Family member name as it appears on website
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"//img[@alt='amily member name']")))      # <- replace with Family member name as it appears on website 
    element.click()

    #Select Screen time
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//body/div["\
            "@id='page-wrapper']/div[@id='main-content-landing']/div[@id='Fami"\
            "lyLandingPage']/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1"\
            "]/div[1]/div[3]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/div[1]/but"\
            "ton[1]")))
    element.click()

    #Set Device limits -> start by clicking on Sunday
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Sunday']")))
    element.click()

    #Select dropdown and select Everyday
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//body/div["\
            "4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]"\
            "/div[1]/span[2]")))
    element.click()
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//body/div[5"\
            "]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/div[1"\
            "]/i[1]")))
    element.click()
    #Simply click outside to escape the dropdown
    driver.find_element_by_xpath("//body").click()

    #Reduce the time to zero
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//body/div[4"\
            "]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/"\
            "div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")))
    action = ActionChains(driver)
    action.click_and_hold(element).move_by_offset(-400, 0).release().perform()

    #Hit Done
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//body[1]/di"\
            "v[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div["\
            "1]/span[1]/button[1]/span[1]/span[1]/span[1]")))
    element.click()

    #Select App and Games
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"//body/div[@"\
            "id='page-wrapper']/div[@id='main-content-landing']/div[@id='Famil"\
            "yLandingPage']/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]"\
            "/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/nav[1]/div[1]/div[1]/"\
            "button[2]/span[1]/span[1]/span[1]")))
    driver.execute_script("arguments[0].click();", element)
#   element.click()

    #start blocking apps one by one
    block_app("discord", driver, wait)
    block_app("whatsapp", driver, wait)
    # ... add more apps that need to be blocked

    sys.stderr.write("Success")
    driver.close()

#Search the app by name and block it
def block_app(name, driver, wait):

    #Click on Show all (some apps may be hidden behind collapse)
    element = wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'Show all')]")))
    element.click()

    #Click on provided App name
    xpath_string = "//*[text()='" + name + "']"
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_string)))
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_string)))
#   element.click()
    driver.execute_script("arguments[0].click();", element)

    try:
        element = driver.find_element(By.XPATH,"//*[text()='Block app']")
        element.click()
    except NoSuchElementException as exception:
        print("App " + name + " already blocked")


    element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='To apps and games']")))
    driver.execute_script("arguments[0].click();", element)
#   element.click()
