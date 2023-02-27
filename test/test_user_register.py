import os
import time
import yaml
from selenium import webdriver
import pytest
from new_admin_demo.Utils.get_path import get_par_path
from new_admin_demo.Utils.read_yml import get_yaml_data
from new_admin_demo.pages.page_newadmin import *
import allure

class Testcase_userregister:
    @allure.step('从配置文件中读取登陆数据')
    @pytest.fixture()
    def login_data(self):
        yaml_path = os.path.join(get_par_path(), "config/config.yaml")
        test_data = get_yaml_data(yaml_path)
        return test_data

    @allure.feature('登录功能')
    @allure.step("使用管理员身份登录")
    def test_login(self, driver, login_data):
        driver.get(login_data['baseurl'])
        driver.maximize_window()
        driver.implicitly_wait(30)
        with allure.step("初始化登录页面"):
            login_page = Locator_Login(driver)
        login_page.click_btn_login_btn()
        login_page.enter_keyword_login_name(login_data['login_name'])
        login_page.enter_keyword_login_pw(login_data['login_pw'])
        login_page.click_btn_login_submit()


# 注册账号
    # 通过邮箱注册
    @allure.story('注册账号')
    @allure.title("通过已有邮箱的账号注册")
    # @pytest.mark.parametrize('mail_list,expect_result',[('1921507475@qq.com,12345','linghuidu15@163.com')])
    @pytest.mark.parametrize('get_data',yaml.safe_load(open('../datafile/test_regto_bymail_account.yaml',encoding='utf-8')))
    def test_regto__bymail_account(self,driver,get_data):
        keyword=get_data['case']
        mail_list=keyword['mail_list']
        # with allure.step("初始化通过已有邮箱的账号注册"):
        Reg_to_account=Locator_reg_to_account(driver)
        with allure.step("进入注册账号页面"):
            Reg_to_account.click_user()
            Reg_to_account.click_registmanage()
            Reg_to_account.click_regto_account()
        with allure.step("选择通过邮件注册"):
            Reg_to_account.enter_keyword_bymail_list(mail_list)
        with allure.step("注册到子机构"):
            Reg_to_account.click_regist_to()
            Reg_to_account.click_select_regist_to()
        with allure.step("选择2个角色"):
            Reg_to_account.click_role()
            Reg_to_account.click_select_role1()
            Reg_to_account.click_select_role2()
        Reg_to_account.click_next_btn()
        Reg_to_account.click_regto_account_save_btn()
        time.sleep(2)
        # with allure.step("初始化结果页面"):
        resultpage=UsermanageResultPage(driver)
        with allure.step("判断账号是否注册成功并截图"):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'regto_bymail.png'
            resultpage.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            # assert 'linghuidu15@163.com' in resultpage.get_regto_account()
            assert '1921507475@qq.com' in resultpage.get_regto_account()

    # 编辑注册账号
    @allure.story('注册账号')
    @allure.title("编辑注册账号")
    def test_edit_reg_to_account(self,driver):
        # with allure.step("初始化修改注册账号页面"):
        Edit_reg_to_account=Locator_edit_reg_to_account(driver)
        Reg_to_account = Locator_reg_to_account(driver)
        with allure.step("进入修改注册账号页面"):
            Reg_to_account.click_regto_account_pop_closebtn()
            # Edit_reg_to_account.click_user()
            Edit_reg_to_account.click_registmanage()
            Edit_reg_to_account.click_change_org()
            Edit_reg_to_account.click_select_change_org()
            Edit_reg_to_account.click_more_option()
            time.sleep(2)
            Edit_reg_to_account.click_edit_regto_account()
        with allure.step("取消一个选择的角色"):
            Edit_reg_to_account.click_close_role()
            Edit_reg_to_account.click_edit_save_btn()
            time.sleep(2)
        # with allure.step("初始化结果页面"):
        resultpage = UsermanageResultPage(driver)
        with allure.step("判断注册的账号是否修改成功并截图"):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'edit_regto_user.png'
            resultpage.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert '注册关系已修改' in resultpage.get_edit_regto_account()


    # 移除注册账号
    @allure.story('注册账号')
    @allure.title("移除注册账号")
    def test_remove_regto_account(self,driver):
        # with allure.step("移除注册账号页面"):
        Remove_reg_to_account=Locator_remove_regto_account(driver)
        Edit_reg_to_account = Locator_edit_reg_to_account(driver)
        with allure.step("进入移除注册账号页面"):
            Edit_reg_to_account.click_edit_regto_account_pop_closebtn()
            Remove_reg_to_account.click_more_option()
            time.sleep(2)
            Remove_reg_to_account.click_remove_regto_account()
        with allure.step("勾选邮件通知"):
            Remove_reg_to_account.click_post_mail()
            Remove_reg_to_account.click_remove_save_btn()
        # with allure.step("初始化结果页面"):
        resultpage=UsermanageResultPage(driver)
        WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(UsermanageResultPage.remove_regto_acount))
        with allure.step("判断注册的账号是否移除成功并截图"):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'remove_regto_user.png'
            resultpage.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert 'linghuidu@163.com' not in resultpage.get_remove_regto_account()

    #  通过账号注册
    @allure.story('注册账号')
    @allure.title("通过已有账号注册")
    @pytest.mark.parametrize('get_data',yaml.safe_load(open('../datafile/test_regto_by_account.yaml',encoding='utf-8')))
    # @pytest.mark.parametrize('mail,expect_result',[('linghuidu@163.com','1个账号已注册')])
    def test_regto_byaccount(self,driver,get_data):
        keyword=get_data['case']
        mail=keyword['mail']
        # with allure.step("初始化通过已有账号注册页面"):
        Regto_byaccount=Locator_regto_byaccount(driver)
        with allure.step("进入注册账号页面"):
            # Regto_byaccount.click_user()
            # Regto_byaccount.click_registmanage()
            Regto_byaccount.click_regto_account()
        with allure.step("通过账号注册页面"):
            Regto_byaccount.click_by_account()
            Regto_byaccount.click_exist_account()
            Regto_byaccount.enter_keyword_search_user(mail)
        Regto_byaccount.click_confirm_btn()
        with allure.step("选择存在的用户"):
            Regto_byaccount.click_choose_user()
            time.sleep(2)
            Regto_byaccount.click_confirm_btn()
        with allure.step("选择2个角色"):
            Regto_byaccount.click_role()
            Regto_byaccount.click_select_role1()
            Regto_byaccount.click_select_role2()
            Regto_byaccount.click_next_btn()
        # with allure.step("初始化结果页面"):
        result_page=UsermanageResultPage(driver)
        time.sleep(1)
        with allure.step("判断注册的账号是否成功并截图"):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'regto_byaccount.png'
            result_page.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert '1 个账号已注册' in result_page.get_regto_account()
    #
    # # 删除用户操作
    @allure.story('账号管理')
    @allure.title("删除用户")
    @pytest.mark.parametrize('get_data',yaml.safe_load(open('../datafile/test_delete_user.yaml',encoding='utf-8')))
    # @pytest.mark.parametrize('keyword,expect_result',[('删除账号','linghuidu@163.com')])
    def test_delete_user(self,driver,get_data):
        keyword=get_data['case']
        input=keyword['keyword']
        # with allure.step("初始化删除用户页面"):
        Regto_byaccount = Locator_regto_byaccount(driver)
        Delete_user=Locator_Delete_Createuser(driver)
        with allure.step("进入删除用户界面"):
            Regto_byaccount.click_regto_account_pop_closebtn()
            Delete_user.click_account_manage()
            Delete_user.click_btn_more_usermanage_option()
            time.sleep(2)
            Delete_user.click_btn_delete()
        with allure.step("点击勾选邮件"):
            Delete_user.click_btn_del_mail()
        with allure.step("输入“删除账号”的文本"):
            Delete_user.enter_keyword_del_input(input)
            Delete_user.click_del_btn()
        # with allure.step("初始化结果页面"):
        result_page = UsermanageResultPage(driver)
        time.sleep(2)
        with allure.step("判断删除用户是否成功并截图"):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'delete_user.png'
            result_page.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert 'linghuidu15@163.com' not in result_page.get_accountmanage()


