from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome('C:/Users/user/pyprojects/lib/chromedriver.exe')
def signup(driver,mail,name,user,passw,year,month,day):
    try:
        driver.get('https://www.instagram.com/accounts/emailsignup/')
        emailphone= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='emailOrPhone']")))
        fullname= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='fullName']")))
        username= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        emailphone.clear()
        emailphone.send_keys(mail)
        time.sleep(2)
        fullname.clear()
        fullname.send_keys(name)
        time.sleep(2)
        username.clear()
        username.send_keys(user)
        time.sleep(2)
        #err=driver.find_element_by_xpath("//span[@class='coreSpriteInputError gBp1f']")
        time.sleep(2)
        password.clear()
        password.send_keys(passw)
        submit= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        time.sleep(3)
        selec=Select(driver.find_element_by_xpath("//select[@title='Year:']"))
        selec.select_by_value(year)
        selec=Select(driver.find_element_by_xpath("//select[@title='Day:']"))
        selec.select_by_value(day)
        selec=Select(driver.find_element_by_xpath("//select[@title='Month:']"))
        selec.select_by_value(month)			
        next= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='sqdOP  L3NKy _4pI4F  y3zKF     ']"))).click()
        time.sleep(60)
        confirmation=input("enter confirmation code:")
        confirm= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email_confirmation_code']")))
        confirm.clear()
        confirm.send_keys(confirmation)
        time.sleep(5)
        newState= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        print("signed up successfully")
    except Exception:
        print("did not confirmed")


def login(driver,user,passw):
    try:
        driver.get('https://www.instagram.com/')
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username.clear()
        #username_of_any_instagram_acount
        username.send_keys(user)
        password.clear()
        #password_of_that_acount
        password.send_keys(passw)
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
        not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
        print("logged in successfully")
    except Exception:
        print("did not logged in")


def message(driver,contact_id, message_text):
    try:
        driver.get('https://www.instagram.com/direct/inbox/')
        time.sleep(5)
        send_message= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='wpO6b ZQScA ']"))).click()
        contact= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='queryBox']")))
        contact.clear()
        contact.send_keys(contact_id)
        contact_list=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="dCJp8 "]'))).click()
        time.sleep(5)
        next= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='sqdOP yWX7d    y3zKF   cB_4K  ']"))).click()
        message_box= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"textarea[placeholder='Message...']")))
        message_box.clear()
        message_box.send_keys(message_text)
        send= WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Send")]'))).click()
        print("message sent")
    except Exception:
        print("not sent")

