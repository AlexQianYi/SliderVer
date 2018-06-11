from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Firefox(executable_path='/Users/yiqian/Downloads/geckodriver')

dr.get('https://account.ch.com/NonRegistrations-Regist')
WebDriverWait(dr, 60).until(
    Expect.visibility_of_element_located((By.CSS_SELECTOR, "div[data-target='account-login"))
)

email = dr.find_element_by_css_selector("div[data-target='account-login']")
email.click()

WebDriverWait(dr, 60).until(
    Expect.visibility_of_element_located((By.ID, "emailRegist"))
)

register = dr.find_element_by_id("emailRegist")
register.click()

"""
offset = get_gap_offset(browser)
drag_and_drop(dr, offset)
"""


print('Browser will be closed')
