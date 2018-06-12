# coding:utf8

from selenium import webdriver
import time as t
import utility
import urllib

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
        bg_file_data = urllib.request.urlopen(bg_img_url).read()
        slider_file_data = urllib.request.urlopen(slider_img_url).read()

        f_bg = open(utility.bg_img_file + bg_file_name, 'wb')
        f_slider = open(utility.slider_img_file + slider_file_name, 'wb')

        f_bg.write(bg_file_data)
        f_slider.write(slider_file_data)

        f_bg.close()
        f_slider.close()

    dr.close()


if __name__ == "__main__":

    get_bg_slider_img(1)

