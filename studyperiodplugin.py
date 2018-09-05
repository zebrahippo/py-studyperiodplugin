# -*- coding:utf-8 -*-

import time
import random
from selenium import webdriver

def main():
    #xiamen机动车驾驶员培训社会公众平台登录界面网址，目前就测试过xiamen的，别的地方的没测
    url = 'http://www.jppt.com.cn/gzpt/index/newLogin'

    try:
        fireFoxOptions = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(firefox_options=fireFoxOptions)
        browser.maximize_window()
        browser.implicitly_wait(6)
        browser.get(url)
        
        #手动输入账户信息，并根据网页当前的验证码输入验证码
        username = raw_input(unicode('用户名：','utf-8').encode('gbk'))
        password = raw_input(unicode('密  码：','utf-8').encode('gbk'))
        verifycode = raw_input(unicode('验证码：','utf-8').encode('gbk'))

        ##用户名 密码 
        elem_username = browser.find_element_by_id('UserName')
        elem_username.send_keys(username)
        elem_pwd = browser.find_element_by_id('Pwd')
        elem_pwd.send_keys(password)
        elem_verifycode = browser.find_element_by_id('VerifyCode')
        elem_verifycode.send_keys(verifycode)
        

        commit = browser.find_element_by_xpath('//*[@id="myform"]/ul/li[6]/input')
        commit.click()

        time.sleep(3)

        #总挂机分钟数
        total_mins = 0
	err = 0

        while True:
            reset_mins = random.randint(12,14)

            #开始计时
            browser.find_element_by_xpath('//*[@id="startTrain"]').click()
            #休眠reset_mins分钟
            time.sleep(reset_mins*60+1)
            #结束计时
            browser.find_element_by_xpath('//*[@id="startTrain"]').click()

            time.sleep(3)

            try:
                #获取confirm对话框
                dialog_box = browser.switch_to_alert()
                #点击【确认】
                dialog_box.accept()
                time.sleep(3)
            except:
		err += 1
            else:
                total_mins += reset_mins+1
		print total_mins

            #超过240分钟结束循环，因为每天最多有效学时240分钟（4小时）
            if total_mins >= 240 or err >= 2:
                break
    except Exception as ex:
        print ex
    finally:
        browser.quit()

if __name__ == '__main__':
    main()
