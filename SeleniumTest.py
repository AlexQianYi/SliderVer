from selenium import webdriver
import time as t
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import utility

dr = webdriver.Firefox(executable_path='/Users/yiqian/Downloads/geckodriver')

dr.get('https://id.163yun.com/login?referrer=https://dun.163.com/dashboard&h=yd&fromyd=baiduP2_YZM_CP1934')
t.sleep(5)
# WebDriverWait(dr, 5).until(Expect.text_to_be_present_in_element((By.CSS_SELECTOR,"#TANGRAM__PSP_8__error"),u'请您填写手机/邮箱/用户名'))

print('start find')
slider = dr.find_element_by_class_name('yidun_slider')
slider.click()
t.sleep(3)
img = dr.find_element_by_class_name('yidun_jigsaw')
print(img)

print('click finish')

dr.close()

//*[@id="bg"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[1]

"""
email = dr.find_element_by_css_selector("div[data-target='account-login']")
email.click()
"""
"""
PhoneNumberInput = dr.find_element_by_name("phoneNumberInput")
PhoneNumberInput.send_keys(utility.PhoneNumer)

GetVerCodeButton = dr.find_element_by_id('getDynamicPwd')
GetVerCodeButton.click()


WebDriverWait(dr, 60).until(
    Expect.visibility_of_element_located((By.ID, "emailRegist"))
)

register = dr.find_element_by_id("emailRegist")
register.click()

offset = get_gap_offset(browser)
drag_and_drop(dr, offset)
"""


print('Browser will be closed')
