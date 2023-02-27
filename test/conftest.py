import os.path
import sys

import pytest
import allure
from selenium import webdriver
from ..Utils.get_path import get_par_path
from ..pages.page_newadmin import Locator_Logout_user


@allure.feature('打开浏览器')
@pytest.fixture(scope='session',autouse=True)
def driver(request):
    driver_path = os.path.join(get_par_path(), "driver/chromedriver")
    driver = webdriver.Chrome(executable_path=driver_path)


    yield driver
    driver.close()
