import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import datetime

def stop_time():
    sleep(3)

dirver=webdriver.Chrome()
dirver.get('http://my.cxxy.seu.edu.cn/')
stop_time()

def login_sys():
    student_id='******'
    student_password='******'
    dirver.find_element_by_id('username').send_keys(student_id)
    dirver.find_element_by_id('password').send_keys(student_password)
    dirver.find_element_by_name('btn').click()
    stop_time()
    dirver.get('http://alstu.cxxy.seu.edu.cn')

def opear_content():

    dirver.get('http://alstu.cxxy.seu.edu.cn/txxm/default.aspx?dfldm=02')
    dirver.find_element_by_link_text("每日健康情况登记").click()


    iframe=dirver.find_element_by_xpath('//*[@id="r_3_3"]')
    dirver.switch_to.frame(iframe)
    dirver.find_element_by_xpath('//*[@id="div0"]/table/tbody/tr[2]/td/img').click()
    stop_time()

    cur_window = dirver.current_window_handle
    dirver.find_element_by_id('rqday').click()
    dirver.find_element_by_id('sfjwhg').click()
    dirver.find_element_by_id('jcjwhg').click()
    dirver.find_element_by_id('jg').click()
    dirver.find_element_by_id('dqdq').click()
    dirver.find_element_by_id('xxdz').send_keys('xxxxxx')
    dirver.find_element_by_id('brjkqk').click()
    dirver.find_element_by_id('sfbljc').click()
    dirver.find_element_by_id('jtcyjk').click()
    stop_time()
    handles=dirver.window_handles
    dirver.switch_to.window(handles[-1])
    dirver.find_element_by_xpath('//*[@id="MyDataGrid"]/tbody/tr[2]').click()
    dirver.switch_to.window(handles[-2])
    dirver.find_element_by_xpath('//*[@id="MyDataGrid"]/tbody/tr[3]').click()
    dirver.switch_to.window(handles[-3])
    dirver.find_element_by_xpath('//*[@id="MyDataGrid"]/tbody/tr[3]').click()
    dirver.switch_to.window(handles[-4])
    dirver.find_element_by_xpath('//*[@id="mh"]').send_keys('360111')
    dirver.find_element_by_xpath('//*[@id="mh"]').send_keys(Keys.ENTER)
    dirver.switch_to.window(handles[-5])
    dirver.find_element_by_xpath('//*[@id="mh"]').send_keys('360111')
    dirver.find_element_by_xpath('//*[@id="mh"]').send_keys(Keys.ENTER)
    dirver.switch_to.window(handles[-6])
    dirver.find_element_by_xpath('//*[@id="MyDataGrid"]/tbody/tr[2]').click()
    dirver.switch_to.window(handles[-7])
    dirver.find_element_by_xpath('//*[@id="MyDataGrid"]/tbody/tr[3]').click()
    dirver.switch_to.window(handles[-8])
    dirver.find_element_by_xpath('//*[@id="MyDataGrid"]/tbody/tr[2]').click()
    time.sleep(20)

    dirver.quit()














    # today=datetime.datetime.today()
    # today=str(today)[:10]
    # print(today)










if __name__=='__main__':
    login_sys()
    opear_content()