import os.path
import sys

import pytest
import allure
from selenium import webdriver

from new_admin_demo.Utils.get_path import get_par_path


@allure.feature('打开浏览器')
@pytest.fixture(scope='session',autouse=True)
def driver(request):
    driver_path = os.path.join(get_par_path(), "driver/chromedriver")
    driver = webdriver.Chrome(executable_path=driver_path)

    def close_browser():
        driver.quit()

    #     无论执行正确和错误最终都执行关闭浏览器的方法
    request.addfinalizer(close_browser)
    return driver

