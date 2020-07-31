from selenium import webdriver
import time
import cv2


# create a new Chrome session
driver = webdriver.Edge(executable_path='browser/msedgedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("https://twitter.com/login")


# get the username textbox
login_field = driver.find_element_by_name("session[username_or_email]")
login_field.clear()

# enter username
login_field.send_keys("prashant.20173@gmail.com")
time.sleep(1)

#get the password textbox
password_field = driver.find_element_by_name("session[password]")
password_field.clear()

#enter password
password_field.send_keys("ASDFGHJKL")
time.sleep(1)
password_field.submit()

time.sleep(1)

logout_but = driver.find_element_by_partial_link_text('logo')
logout_but.click()
print(logout_but)

print("AYA...")
# logout_key = driver.find_element_by_class_name("css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1j3t67a r-9qu9m4 r-o7ynqc r-6416eg r-13qz1uu").click()
# time.sleep(1)



