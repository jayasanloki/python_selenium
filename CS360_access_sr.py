### python version supported 2.7,3.5 or above and selenium version 3.141.0 is used. find_element_by_* is deprecated in selenium 4.* version
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
###from selenium.webdriver.chrome.service import Service
###from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# get mailid and INC reference as input. Once cortex integrated, it will provide INC & mailid as cmd line arguments
username=input('Enter email id of user : ')
inc = input('Enter INC reference : ')
# password with random int
password=username.split('.')[0]+str(random.randrange(1,9))
# method to send email with credentials
def send_mail(username,password,inc):
	fromaddr,toaddr = "TCSEIMServiceSupport@cw.com",username
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = username
	msg['Subject'] =  inc +" - CS360 access"
	part1 = '''Hi '''+toaddr.split('.')[0].title()+''',

CS360 access has been provided to you. PFB credentials for the same,

Username: '''+username
	part2='''
Password : '''+password
	part3='''

Let us know if you face any login issues. 

Thanks,
EIM Team'''
	body=part1+part2+part3
	msg.attach(MIMEText(body, 'plain'))
	s = smtplib.SMTP('appsmtp-north.internal.vodafone.com:25')
	s.ehlo
	text =  msg.as_string()
	###s.sendmail(fromaddr, (toaddr+tocc).split(';'), text)
	s.sendmail(fromaddr, toaddr.split(';'), text)

# Istalls chromedriver in cache and run the actions
###s=Service(ChromeDriverManager().install())
###driver = webdriver.Chrome(service=s)

# create webdriver object using local chromedriver downloaded from google - should match the version of chrome installed
driver=webdriver.Chrome(executable_path="C:\\Users\\KumarL1\\Downloads\\chromedriver.exe")
# since using loop, mail will be dropped twice to user. with this varible we can send only once
m=0
# load balancing URLs and dictionary for exception message.
urls={}
urls["server 1"]="https://:8443/ontoscope/Sysadmin"
urls["server 2"]="https://:8443/ontoscope/Sysadmin"
# using loop for above URLs with same id's on all elements
for i in urls.keys():
        driver.get(urls[i])
        driver.maximize_window()
        # handle browser security exception page
        ActionChains(driver).click(driver.find_element_by_id("details-button")).perform()
        ActionChains(driver).click(driver.find_element_by_id("proceed-link")).perform()
        # login page
        ActionChains(driver).click(driver.find_element_by_id("id1")).send_keys("").perform()
        ActionChains(driver).click(driver.find_element_by_name("fragment:password")).send_keys("").perform()
        ActionChains(driver).click(driver.find_element_by_id("id3")).perform()
        # sysadmin page navigate to users page
        ActionChains(driver).click(driver.find_element_by_link_text("Users")).perform()
        # handle popup user form window using below attribute
        main_page = driver.current_window_handle
        login_page=''
        ###wait=WebDriverWait(driver,3)
        # wait till the DOM loads for the navigation menu of USERS tab
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add User']"))).click()
        for handle in driver.window_handles:
                if handle != main_page:
                        login_page = handle
        driver.switch_to.window(login_page)
        # wait till the DOM loads for the popup user details form
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idc5']")))
        # user details
        ActionChains(driver).click(driver.find_element_by_name("username")).send_keys(username).perform()
        ActionChains(driver).click(driver.find_element_by_id("user-email")).send_keys(username).perform()
        ActionChains(driver).click(driver.find_element_by_name("password")).send_keys(password).perform()
        ActionChains(driver).click(driver.find_element_by_name("passwordConfirm")).send_keys(password).perform()
        print('password : '+password)
        myOption = driver.find_element_by_xpath("//select[@multiple]/option[contains(text(), 'browser')]")
        myOption1 = driver.find_element_by_xpath("//select[@multiple]/option[contains(text(), 'Vodafone UK CSM')]")
        ActionChains(driver).key_down(Keys.CONTROL).click(myOption).key_up(Keys.CONTROL).perform()
        ActionChains(driver).key_down(Keys.CONTROL).click(myOption1).key_up(Keys.CONTROL).perform()
        ActionChains(driver).click(driver.find_element_by_xpath("//*[@id='idb6']/div[2]/input[1]")).perform()
        # wait till the DOM loads the previous page or handle exception
        try:
                wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log Out']"))).click()
                m=m+1
                if m==2:
                        send_mail(username,password,inc)
        except ElementClickInterceptedException:
                print('User already exists in '+ i)
                # Eventhough the exception is handled, closing the session by cancelling user form and logout. Since ontology is limited to 5 admin sessions only
                ActionChains(driver).click(driver.find_element_by_name("newUserSubmit:cancel")).perform()
                wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log Out']"))).click()
                break
# close the driver object
driver.close();

#EOF#
