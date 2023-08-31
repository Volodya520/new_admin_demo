import os
import time
import pytest
from new_admin_demo.Utils.get_path import get_par_path
from new_admin_demo.Utils.read_yml import get_yaml_data
import allure
from new_admin_demo.pages.page_newadmin import *



# sd反反复复反反复复付额外

class Testcase_userregister(object):
    @allure.step('从配置文件中读取登陆数据')
    @pytest.fixture()
    def login_data(self):
        # self.log=conf.logcon()
        # self.log.info(("read_config.yaml"))
        yaml_path = os.path.join(get_par_path(), "config/user_register_config.yaml")
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
        login_page.click_login_btn()
        login_page.enter_keyword_login_name(login_data['login_name'])
        login_page.enter_keyword_login_pw(login_data['login_pw'])
        login_page.click_login_submit()

    @allure.story('账号管理')
    @allure.title("创建账号")
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_create_user2.yaml', encoding='utf-8')))
    def test_create_user(self, driver, get_data):
        keyword = get_data['case2']
        fullname = keyword['fullname']
        displayname = keyword['displayname']
        SIS_ID = keyword['SIS_ID']
        mail = keyword['mail']
        new_pw = keyword['new_pw']
        with allure.step("进入用户模块页面"):
            # 增加前端css添加可复制文本属性
            Create_user = Locator_Create_user(driver)
        with allure.step('进入创建账号的弹窗'):
            Create_user.click_accountmanage()
            is_leaf = driver.find_elements(By.CLASS_NAME, "is-leaf")
            Create_user.css_text(is_leaf)
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_userregister\\')
            usermanage_notranslation = pic_path + 'usermanage_notranslation.png'
            Create_user.keyword_key(usermanage_notranslation)
            allure.attach.file(usermanage_notranslation, attachment_type=allure.attachment_type.PNG)
            Create_user.click_user_create()
            elements = driver.find_elements(By.CLASS_NAME, 'el-button')
            Create_user.css_text(elements)
            createuser_notranslation = pic_path + 'useroperation_notranslation.png'
            Create_user.keyword_key(createuser_notranslation)
            allure.attach.file(createuser_notranslation, attachment_type=allure.attachment_type.PNG)
            Create_user.enter_keyword_create_full_name(fullname)
            Create_user.enter_keyword_create_displayname(displayname)
            Create_user.enter_keyword_create_SIS_ID(SIS_ID)
            Create_user.enter_keywords_create_mail(mail)
            Create_user.enter_keyword_create_new_pw(new_pw)
            time.sleep(2)
            Create_user.click_create_user_role()
            time.sleep(2)
            Create_user.click_create_select_role()
            Create_user.click_create_otherthing()
            Create_user.click_create_btn()
        with allure.step('完成创建账号'):
            creprompt_notranslation= pic_path + 'creprompt_notranslation.png'
            Create_user.keyword_key(creprompt_notranslation)
            allure.attach.file(createuser_notranslation, attachment_type=allure.attachment_type.PNG)


# 注册账号
    # 通过邮箱注册
    @allure.story('注册账号')
    @allure.title("通过已有邮箱的账号注册")
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_regto_bymail_account.yaml', encoding='utf-8')))
    def test_regto__bymail_account(self,driver,get_data):
        keyword=get_data['case']
        mail_list=keyword['mail_list']
        Reg_to_account=Locator_reg_to_account(driver)
        with allure.step("进入注册账号页面"):
            Reg_to_account.click_user()
            Reg_to_account.click_registmanage()
            is_leaf=driver.find_elements(By.CLASS_NAME,"is-leaf")
            Reg_to_account.css_text(is_leaf)
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_userregister\\')
            userregist_notranslation = pic_path + 'userregist_notranslation.png'
            Reg_to_account.keyword_key(userregist_notranslation)
            allure.attach.file(userregist_notranslation, attachment_type=allure.attachment_type.PNG)
            Reg_to_account.click_regto_account()
            el_button=driver.find_elements(By.CLASS_NAME,"el-button")
            Reg_to_account.css_text(el_button)
            regto_account_notranslation1 = pic_path + 'regto_account_notranslation1.png'
            Reg_to_account.keyword_key(regto_account_notranslation1)
            allure.attach.file(regto_account_notranslation1, attachment_type=allure.attachment_type.PNG)
            Reg_to_account.enter_keyword_bymail_list(mail_list)
            Reg_to_account.click_regist_to()
            time.sleep(2)
            Reg_to_account.click_select_regist_to()
            Reg_to_account.click_role()
            Reg_to_account.click_select_role1()
            Reg_to_account.click_select_role2()
        with allure.step('进入注册账号页面第2步'):
            Reg_to_account.click_next_btn()
            regto_account_notranslation2 = pic_path + 'regto_account_notranslation2.png'
            Reg_to_account.keyword_key(regto_account_notranslation2)
            allure.attach.file(regto_account_notranslation2, attachment_type=allure.attachment_type.PNG)
        with allure.step('完成注册账号'):
            Reg_to_account.click_regto_account_save_btn()
            regtoaccount_result_notranslation = pic_path + 'regtoaccount_result_notranslation.png'
            Reg_to_account.keyword_key(regtoaccount_result_notranslation)
            allure.attach.file(regtoaccount_result_notranslation, attachment_type=allure.attachment_type.PNG)
            Reg_to_account.click_regto_account_pop_closebtn()




    # 编辑注册账号
    @allure.story('注册账号')
    @allure.title("编辑注册账号")
    @pytest.mark.parametrize("get_data", yaml.safe_load(open('../datafile/test_datatext/test_edit_regto_account.yaml', encoding='utf-8')))
    def test_edit_regto_account(self,driver,get_data):
        keyword=get_data['case']
        input=keyword['search_mail']
        Edit_reg_to_account=Locator_edit_reg_to_account(driver)
        Edit_reg_to_account.click_user()
        Edit_reg_to_account.click_registmanage()
        Edit_reg_to_account.click_change_org()
        Edit_reg_to_account.click_select_change_org()
        time.sleep(2)
        Edit_reg_to_account.enter_keyword_search_account(input)
        Edit_reg_to_account.click_user()
        time.sleep(2)
        Edit_reg_to_account.click_more_option()
        time.sleep(2)
        Edit_reg_to_account.click_edit_regto_account()
        with allure.step('进入修改注册账号界面'):
            el_button=driver.find_elements(By.CLASS_NAME,"el-button")
            Edit_reg_to_account.css_text(el_button)
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_userregister\\')
            edit_regto_account = pic_path + 'edit_regto_account.png'
            Edit_reg_to_account.keyword_key(edit_regto_account)
            allure.attach.file(edit_regto_account, attachment_type=allure.attachment_type.PNG)
            Edit_reg_to_account.click_close_role()
        with allure.step('完成修改注册用户操作'):
            Edit_reg_to_account.click_edit_save_btn()
            edit_registuser_pop_notranslation = pic_path + 'edit_registuser_pop_notranslation.png'
            Edit_reg_to_account.keyword_key(edit_registuser_pop_notranslation)
            allure.attach.file(edit_registuser_pop_notranslation, attachment_type=allure.attachment_type.PNG)
            Edit_reg_to_account.click_edit_regto_account_pop_closebtn()


    # 移除注册账号
    @allure.story('注册账号')
    @allure.title("移除注册账号")
    @pytest.mark.parametrize("get_data",yaml.safe_load(open('../datafile/test_datatext/test_edit_regto_account.yaml', encoding='utf-8')))
    def test_remove_regto_account(self,get_data,driver):
        Remove_reg_to_account=Locator_remove_regto_account(driver)
        with allure.step("进入移除注册账号页面"):
            Remove_reg_to_account.click_user()
            Remove_reg_to_account.click_registmanage()
        with allure.step("操作查找到的账号"):
            Remove_reg_to_account.click_more_option()
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_userregister\\')
            registmanage_moreoption_notranslation = pic_path + 'registmanage_moreoption.png'
            Remove_reg_to_account.keyword_key(registmanage_moreoption_notranslation)
            allure.attach.file(registmanage_moreoption_notranslation, attachment_type=allure.attachment_type.PNG)
            time.sleep(2)
        with allure.step("删除注册账号"):
            Remove_reg_to_account.click_remove_regto_account()
            model_content=driver.find_elements(By.CLASS_NAME,"model-content")
            el_checkbox_label=driver.find_elements(By.CLASS_NAME,"el-checkbox")
            Remove_reg_to_account.css_text(model_content)
            Remove_reg_to_account.css_text(el_checkbox_label)
            remove_regto_account_notranslation = pic_path + 'remove_regto_account.png'
            Remove_reg_to_account.keyword_key(remove_regto_account_notranslation)
            allure.attach.file(remove_regto_account_notranslation, attachment_type=allure.attachment_type.PNG)
        with allure.step("完成注册账号"):
            Remove_reg_to_account.click_post_mail()
            Remove_reg_to_account.click_remove_save_btn()
            remove_regto_account_prompt_notranslation = pic_path + 'remove_regto_account_prompt_notranslation.png'
            Remove_reg_to_account.keyword_key(remove_regto_account_prompt_notranslation)
            allure.attach.file(remove_regto_account_prompt_notranslation, attachment_type=allure.attachment_type.PNG)



#     #  通过账号注册
    @allure.story('注册账号')
    @allure.title("通过已有账号注册")
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_regto_by_account.yaml', encoding='utf-8')))
    def test_regto_byaccount(self,driver,get_data):
        keyword=get_data['case']
        mail=keyword['mail']
        Regto_byaccount=Locator_regto_byaccount(driver)
        with allure.step("进入注册账号页面"):
            Regto_byaccount.click_user()
            Regto_byaccount.click_registmanage()
            Regto_byaccount.click_regto_account()
        with allure.step("通过账号注册页面"):
            Regto_byaccount.click_by_account()
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_userregister\\')
            regto_byaccount_notranslation = pic_path + 'regto_byaccount_notranslation.png'
            Regto_byaccount.keyword_key(regto_byaccount_notranslation)
            allure.attach.file(regto_byaccount_notranslation, attachment_type=allure.attachment_type.PNG)
            Regto_byaccount.click_exist_account()
            Regto_byaccount.enter_keyword_search_user(mail)
            Regto_byaccount.click_confirm_sear_result()
        with allure.step("选择存在的用户"):
            Regto_byaccount.click_choose_user()
            time.sleep(2)
            elements = driver.find_elements(By.CLASS_NAME, 'el-button')
            Regto_byaccount.css_text(elements)
            chooseuser_notranslation= pic_path + 'chooseuser_notranslation.png'
            Regto_byaccount.keyword_key(chooseuser_notranslation)
            Regto_byaccount.click_confirm_btn()
        with allure.step("选择2个角色"):
            Regto_byaccount.click_role()
            Regto_byaccount.click_select_role1()
            Regto_byaccount.click_select_role2()
            Regto_byaccount.click_next_btn()
            regtoaccount_bymail_result_notranslation = pic_path + 'regtoaccount_bymail_result_notranslation.png'
            Regto_byaccount.keyword_key(regtoaccount_bymail_result_notranslation)
            allure.attach.file(regtoaccount_bymail_result_notranslation, attachment_type=allure.attachment_type.PNG)

