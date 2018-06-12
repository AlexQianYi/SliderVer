# coding:utf8

import requests
from selenium import webdriver
import time as t
import utility
import urllib
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

bg_img_dic = {}
slider_img_dic = {}

def get_bg_slider_img(m):

    # bg img xpath
    bg_xpath = '//*[@id="bg"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[1]'
    # slider img xpath
    slider_xpath = '//*[@id="bg"]/div[2]/div/div/div/div/div[1]/form/div[3]/div/div/div[1]/div/div[1]/img[2]'

    # launch firefox
    dr = webdriver.Firefox(executable_path=utility.firefox_driver_path)

    # record the image have loaded
    global bg_img_dic, slider_img_dic

    # start firefox
    dr.get(utility.url)
    t.sleep(5)

    bg_img_element = dr.find_element_by_xpath(bg_xpath)
    slider_img_element = dr.find_element_by_xpath(slider_xpath)

    bg_img_url = bg_img_element.get_attribute('src')
    slider_img_url = slider_img_element.get_attribute('src')

    if bg_img_url != None and not bg_img_url in bg_img_dic:

        bg_img_dic[bg_img_url] = ''
        slider_img_dic[slider_img_url] = ''

        bg_img_ext = bg_img_url.split('.')[-1]                      # .jpg
        slider_img_ext = slider_img_url.split('.')[-1]              # .png

        bg_file_name = str(m) + '.' + bg_img_ext
        slider_file_name = str(m) + '.' + slider_img_ext

        # save image file
        bg_file_data = urllib.

        print(bg_img_ext)
        print(slider_img_ext)


if __name__ == "__main__":

    get_bg_slider_img(1)


"""

# WebDriverWait(dr, 5).until(Expect.text_to_be_present_in_element((By.CSS_SELECTOR,"#TANGRAM__PSP_8__error"),u'请您填写手机/邮箱/用户名'))

print('start find')
slider = dr.find_element_by_class_name('yidun_slider')
slider.click()
t.sleep(3)
img = dr.find_element_by_class_name('yidun_jigsaw')
print(img)

print('click finish')

dr.close()



email = dr.find_element_by_css_selector("div[data-target='account-login']")
email.click()

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


print('Browser will be closed')

download dataset

def downimage(i, FileDes):
    # 构建session
    sess = requests.Session()
    # 建立请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "Connection": "keep-alive"}
    url = "https://account.flycua.com/sso/chineseVerifyCode.images"
    # 获取响应图片内容
    image = sess.get(url, headers=headers).content
    # 保存到本地
    with open(FileDes, "wb") as f:
        f.write(image)


if __name__ == "__main__":
    for i in range(1000):
        print('正在下载: ',i+1)
        downimage(i, "./VerPic/" + str(i) + "image.jpg")
        
"""
