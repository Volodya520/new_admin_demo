import logging
import re
import time
import logging
import pyautogui
import pyperclip
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait



log = logging.getLogger("newadmin_notranslation'log")
class BaseAction(object):
    # 后面是是数据类型，这个driver就是浏览器
    def __init__(self, driver):
        # 进行浏览器操作，初始化一定有浏览器
        self.driver = driver
    # 把发现元素方法封装，加上等待步骤
        log.info("驱动初始化")

    def find_element(self, location, timeout=10, poll_frequency=1):
        # By.ID类型 ， 值，加上只能等待
        local_by, local_value = location
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(lambda driver: self.driver.find_element(local_by, local_value))

    def find_elements(self, location, timeout=10, poll_frequency=1):
        # By.ID类型 ， 值，加上只能等待
        local_by, local_value = location
        wait = WebDriverWait(self.driver,timeout,poll_frequency)
        return wait.until(lambda driver: self.driver.find_elements(local_by,local_value))


    def input_things(self,location,text):
        ele = self.find_element(location)
        ele.clear()
        ele.send_keys(text)
        log.info("输入文本信息")


    def click_i(self,location):
        ele = self.find_element(location)
        try:
            ele.click()
            log.info("点击操作")
        except ElementClickInterceptedException:
            self.js_click(ele)


    def js_click(self, location):
        self.driver.execute_script("arguments[0].click()", location)
        log.info("驱动JS强制点击操作")

    def save_picture(self,filepath):
        self.driver.save_screenshot(filepath)
        log.info("截图操作")

    def keyword_key(self,filepath):
        time.sleep(3)
        text_list = []
        pyautogui.hotkey('ctrl', 'a')
        log.info("全选页面文本信息")
        pyautogui.hotkey('ctrl', 'c')
        log.info("复制全选页面文本信息")
        clipboard_content = pyperclip.paste()
        text_list.append(clipboard_content)
        log.info("将复制的文本粘贴到列表中")
        for index, value in enumerate(text_list):
            text_list1 = re.findall(r'[\u4e00-\u9fa5]+', value)
            print(text_list1)
            if len(text_list1) == 0:
                pass
                log.info("没有漏翻译的语言不进行截图操作")
            else:
                self.save_picture(filepath)
                log.info("对于漏翻译的语言进行截图操作")

    def css_text(self,elements):
        for ele in elements:
            self.driver.execute_script("arguments[0].style.userSelect = 'text';", ele)
            log.info("驱动js添加css可复制文本属性")
