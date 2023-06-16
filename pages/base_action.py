from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
class BaseAction(object):
    # 后面是是数据类型，这个driver就是浏览器
    def __init__(self, driver):
        # 进行浏览器操作，初始化一定有浏览器
        self.driver = driver
    # 把发现元素方法封装，加上等待步骤

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

    def click_i(self,location):
        ele = self.find_element(location)
        try:
            ele.click()
        except ElementClickInterceptedException:
            self.js_click(ele)

    def js_click(self, location):
        self.driver.execute_script("arguments[0].click()", location)

    def save_picture(self,filepath):
        self.driver.save_screenshot(filepath)


