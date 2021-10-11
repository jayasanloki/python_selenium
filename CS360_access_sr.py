from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username=input('Enter email id of user : ')
password=username.split('.')[0]
inc = input('Enter INC reference :')
# create webdriver object
driver=webdriver.Chrome(executable_path="C:\\Users\\KumarL1\\Downloads\\chromedriver.exe")

#server1
driver.get("")
driver.maximize_window()

element = driver.find_element_by_id("details-button")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

element = driver.find_element_by_id("proceed-link")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

element = driver.find_element_by_id("id1")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys("")
action.perform()

element = driver.find_element_by_name("fragment:password")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys("")
action.perform()

element = driver.find_element_by_id("id3")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

element = driver.find_element_by_link_text("Users")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

main_page = driver.current_window_handle
login_page=''
#wait=WebDriverWait(driver,3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add User']"))).click()

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

driver.switch_to.window(login_page)

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idc5']")))

element = driver.find_element_by_name("username")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys(username)
action.perform()

element = driver.find_element_by_id("user-email")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys(username)
action.perform()

element = driver.find_element_by_name("password")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys(password)
action.perform()

element = driver.find_element_by_name("passwordConfirm")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys(password)
action.perform()

print(password)

myOption = driver.find_element_by_xpath("//select[@multiple]/option[contains(text(), 'browser')]")
myOption1 = driver.find_element_by_xpath("//select[@multiple]/option[contains(text(), 'Vodafone UK CSM')]")

ActionChains(driver).key_down(Keys.CONTROL).click(myOption).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(myOption1).key_up(Keys.CONTROL).perform()

element = driver.find_element_by_xpath("//*[@id='idb6']/div[2]/input[1]")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log Out']"))).click()

#server2
driver.get("")
driver.maximize_window()

element = driver.find_element_by_id("details-button")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

element = driver.find_element_by_id("proceed-link")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

element = driver.find_element_by_id("id1")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys("")
action.perform()

element = driver.find_element_by_name("fragment:password")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys("")
action.perform()

element = driver.find_element_by_id("id3")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

element = driver.find_element_by_link_text("Users")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

main_page = driver.current_window_handle
login_page=''
#wait=WebDriverWait(driver,3)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Add User']"))).click()

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

driver.switch_to.window(login_page)

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='idc5']")))

element = driver.find_element_by_name("username")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys(username)
action.perform()

element = driver.find_element_by_id("user-email")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys(username)
action.perform()

element = driver.find_element_by_name("password")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys(password)
action.perform()

element = driver.find_element_by_name("passwordConfirm")
action = ActionChains(driver)
action.click(on_element = element)
action.send_keys(password)
action.perform()

print(password)

myOption = driver.find_element_by_xpath("//select[@multiple]/option[contains(text(), 'browser')]")
myOption1 = driver.find_element_by_xpath("//select[@multiple]/option[contains(text(), 'Vodafone UK CSM')]")

ActionChains(driver).key_down(Keys.CONTROL).click(myOption).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(myOption1).key_up(Keys.CONTROL).perform()

element = driver.find_element_by_xpath("//*[@id='idb6']/div[2]/input[1]")
action = ActionChains(driver)
action.click(on_element = element)
action.perform()

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log Out']"))).click()

driver.close();

#send email

fromaddr = "lokesh.kumar@vodafone.com"
toaddr=username
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = username
msg['Subject'] =  inc +" - CS360 access"
pwd = password
part1 = '''Hi '''+toaddr.split('.')[0].title()+''',

CS360 access has been provided to you. PFB credentials for the same,

Username: '''+username

part2='''
Password : '''+pwd

part3='''

Let us know if you face any login issues. 

Thanks,
EIM Team'''

body=part1+part2+part3
msg.attach(MIMEText(body, 'plain'))
s = smtplib.SMTP(':25')
s.ehlo
text =  msg.as_string()
#s.sendmail(fromaddr, (toaddr+tocc).split(';'), text)
s.sendmail(fromaddr, toaddr.split(';'), text)
