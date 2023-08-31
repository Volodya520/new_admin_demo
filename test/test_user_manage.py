import logging
import os
import time
import pytest
from new_admin_demo.Utils.get_path import get_par_path
from new_admin_demo.Utils.log import conf
from new_admin_demo.Utils.read_yml import get_yaml_data
from new_admin_demo.pages.page_newadmin import *
import allure
# 123123122121

logging.getLogger('vova')
class TestClass_usermanage(object):
    @allure.step('从配置文件中读取登陆数据')
    @pytest.fixture()
    def login_data(self):
        # self.log=conf.logcon()
        # self.log.info(("read_config.yaml"))
        yaml_path = os.path.join(get_par_path(), "config/user_manage_config.yaml")
        test_data = get_yaml_data(yaml_path)
        return test_data

    @allure.story('登录功能')
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


# 用户模块
    # # #1.txt. 账号管理
    # 邀请用户
    @allure.story('账号管理')
    @allure.title('邀请用户')
    @pytest.mark.parametrize("get_data", yaml.safe_load(open('../datafile/test_datatext/test__invite_user.yaml', encoding='utf-8')))
    def test_invite_user(self,driver,get_data):
        keyword=get_data["case"]
        input=keyword['keyword']
        Invite_user=Locator_invite_user(driver)
        # 检测用户页面漏翻译
        Invite_user.click_user()
        pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_usermanage\\')
        # 检测邀请用户弹窗漏翻译情况
        Invite_user.click_inv_user()
        # 前端组件el-button，css添加可复制文本属性
        elements=driver.find_elements(By.CLASS_NAME,'el-button')
        Invite_user.css_text(elements)
        with allure.step('邀请用户第1步'):
            invite_usernotranslation_path1 = pic_path+ 'invite_usernotranslation1.png'
            Invite_user.keyword_key(invite_usernotranslation_path1)
            allure.attach.file(invite_usernotranslation_path1, attachment_type=allure.attachment_type.PNG)
            Invite_user.enter_keyword_mail_adress(input)
            Invite_user.click_regist_to()
            Invite_user.click_select_regist_to()
            Invite_user.click_role()
            Invite_user.click_select_role()
        with allure.step('邀请用户第2步'):
            # 检测邀请用户第2步弹窗的漏翻译
            Invite_user.click_next_step()
            invite_usernotranslation_path2 = pic_path + 'invite_usernotranslation2.png'
            Invite_user.keyword_key(invite_usernotranslation_path2)
            allure.attach.file(invite_usernotranslation_path2, attachment_type=allure.attachment_type.PNG)
            Invite_user.click_inv_user_save_btn()
            # 结果页面漏翻译检测
        with allure.step("完成邀请用户"):
            invite_user_pop_path = pic_path + 'invite_user_pop.png'
            Invite_user.keyword_key(invite_user_pop_path)


    # 删除账号*****
    @allure.story('账号管理')
    @allure.title('删除待激活的账号')
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_delete_invite_user.yaml', encoding='utf-8')))
    def test_delete_invite_user(self,driver,get_data):
        keyword = get_data["case"]
        input = keyword['keyword']
        Delete_invite_user=Locator_delete_invite_user(driver)
        Invite_user = Locator_invite_user(driver)
        with allure.step('用户账号的操作'):
            Invite_user.click_invite_user_pop_closebtn()
            Delete_invite_user.click_btn_more_usermanage_option()
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_usermanage\\')
            useroperation_notranslation= pic_path + 'useroperation_notranslation.png'
            Delete_invite_user.keyword_key(useroperation_notranslation)
            allure.attach.file(useroperation_notranslation, attachment_type=allure.attachment_type.PNG)
            time.sleep(2)
        with allure.step('点击删除账号按钮'):
            Delete_invite_user.click_btn_delete()
            # 增加前端css添加可复制文本属性

            ele_model_content=driver.find_elements(By.CLASS_NAME,'model-content')
            el_checkbox_label=driver.find_elements(By.CLASS_NAME,"el-checkbox__label")
            Delete_invite_user.css_text(ele_model_content)
            Delete_invite_user.css_text(el_checkbox_label)

            elements = driver.find_elements(By.CLASS_NAME, 'el-button')
            Delete_invite_user.css_text(elements)
            delpop_notranslation= pic_path + 'delpop_notranslation.png'
            Delete_invite_user.keyword_key(delpop_notranslation)
            allure.attach.file(delpop_notranslation, attachment_type=allure.attachment_type.PNG)
            Delete_invite_user.click_btn_del_mail()
            Delete_invite_user.enter_keyword_del_input(input)
            Delete_invite_user.click_del_btn()
        with allure.step("点击删除按钮完成删除"):
            delprompt_notranslation= pic_path + 'delprompt_notranslation.png'
            Delete_invite_user.keyword_key(delprompt_notranslation)
            allure.attach.file(delprompt_notranslation, attachment_type=allure.attachment_type.PNG)



   # 创建账号*****
    @allure.story('账号管理')
    @allure.title("创建账号")
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_create_user.yaml', encoding='utf-8')))
    def test_create_user(self,driver,get_data):
        keyword=get_data['case1']
        fullname=keyword['fullname']
        displayname=keyword['displayname']
        SIS_ID=keyword['SIS_ID']
        mail=keyword['mail']
        new_pw=keyword['new_pw']
        Create_user=Locator_Create_user(driver)
        with allure.step('点击按钮跳出创建账号弹窗'):
            Create_user.click_user_create()
            # 增加前端css添加可复制文本属性
            elements = driver.find_elements(By.CLASS_NAME, 'el-button')
            Create_user.css_text(elements)
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_usermanage\\')
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


    # 编辑账号
    @allure.story('账号管理')
    @allure.title("编辑账号")
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_edit_user.yaml', encoding='utf-8')))
    def test_edit_user(self,driver,get_data):
        keyword=get_data['case']
        fullname=keyword['fullname']
        displayname=keyword['displayname']
        SIS_ID=keyword['SIS_ID']
        mail=keyword['mail']
        Edit_user=Locator_Edit_Createuser(driver)
        Edit_user.click_user()
        Edit_user.click_more_usermanage_option()
        time.sleep(2)
        Edit_user.click_btn_edit_user()
        with allure.step('进入编辑账号页面'):
            #增加前端css添加可复制文本属性
            elements = driver.find_elements(By.CLASS_NAME, 'el-button')
            Edit_user.css_text(elements)
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_usermanage\\')
            edituser_notranslation = pic_path + 'edituser_notranslation.png'
            Edit_user.keyword_key(edituser_notranslation)
            allure.attach.file(edituser_notranslation, attachment_type=allure.attachment_type.PNG)
            Edit_user.click_btn_edit_mail()
            Edit_user.enter_keyword_fullname(fullname)
            Edit_user.enter_keyword_displayname(displayname)
            Edit_user.enter_keyword_SIS_ID(SIS_ID)
            Edit_user.enter_keyword_mail(mail)
            Edit_user.click_btnpost_mail()
            Edit_user.click_edit_save_btn()
        with allure.step('完成编辑账号'):
            edituser_prompt_notranslation = pic_path + ' edituser_prompt_notranslation.png'
            Edit_user.keyword_key(edituser_prompt_notranslation)
            allure.attach.file(edituser_prompt_notranslation, attachment_type=allure.attachment_type.PNG)


   # 修改密码
    @allure.story('账号管理')
    @allure.title("修改密码")
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_edit_pw.yaml', encoding='utf-8')))
    def test_edit_pw(self,driver,get_data):
        keyword=get_data['case']
        new_pw=keyword['new_pw']
        confirm_pw=keyword['confirm_pw']
        Edit_pw=Locator_Edit_Pw(driver)
        with allure.step("进入修改密码页面"):
            Edit_pw.click_user()
            Edit_pw.click_btn_more_usermanage_option()
            time.sleep(2)
            Edit_pw.click_edit_pw()
            # 增加前端css添加可复制文本属性
            elements = driver.find_elements(By.CLASS_NAME, 'el-button')
            Edit_pw.css_text(elements)
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_usermanage\\')
            edit_pw_notranslation = pic_path + 'edit_pw_notranslation.png'
            allure.attach.file(edit_pw_notranslation, attachment_type=allure.attachment_type.PNG)
            Edit_pw.keyword_key(edit_pw_notranslation)
            Edit_pw.enter_keyword_new_pw(new_pw)
            Edit_pw.enter_keyword_confirm_pw(confirm_pw)
            Edit_pw.click_save_btn()
        with allure.step("完成修改密码"):
            editpw_prompt_notranslation = pic_path + 'editpw_prompt_notranslation.png'
            Edit_pw.keyword_key(editpw_prompt_notranslation)
            allure.attach.file(editpw_prompt_notranslation, attachment_type=allure.attachment_type.PNG)


    # 停用
    @allure.story('账号管理')
    @allure.title("停用账号")
    def test_disable_account(self,driver):
        Dis_account= Locator_disable_account(driver)
        Edit_pw = Locator_Edit_Pw(driver)
        Edit_pw.click_edit_pw_suf_pop()
        Dis_account.click_user()
        Dis_account.click_btn_more_usermanage_option()
        time.sleep(2)
        Dis_account.click_dis_account()
        with allure.step('进入停用账号页面'):
            # 增加前端css添加可复制文本属性
            model_content=driver.find_elements(By.CLASS_NAME,'model-content')
            el_checkbox_label=driver.find_elements(By.CLASS_NAME,'el-checkbox__label')
            elements = driver.find_elements(By.CLASS_NAME, 'el-button')
            Dis_account.css_text(model_content)
            Dis_account.css_text(el_checkbox_label)
            Dis_account.css_text(elements)
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_usermanage\\')
            dis_account_notranslation = pic_path + 'dis_account_notranslation.png'
            allure.attach.file(dis_account_notranslation, attachment_type=allure.attachment_type.PNG)
            Dis_account.keyword_key(dis_account_notranslation)
            Dis_account.click_post_mail()
            Dis_account.click_save_btn()
        with allure.step('完成账号停用操作'):
            disaccount_prompt_notranslation = pic_path + 'disaccount_prompt_notranslation.png'
            Dis_account.keyword_key(disaccount_prompt_notranslation)
            allure.attach.file(disaccount_prompt_notranslation, attachment_type=allure.attachment_type.PNG)


    # 激活
    @allure.story('账号管理')
    @allure.title("激活账号")
    def test_active_account(self,driver):
        Active_account=Locator_active_account(driver)
        with allure.step('进入停用账号页面'):
            Active_account.click_user()
            Active_account.click_btn_more_usermanage_option()
            time.sleep(2)
            Active_account.click_act_account()
            # 增加前端css添加可复制文本属性
            model_content=driver.find_elements(By.CLASS_NAME,'model-content')
            el_checkbox_label=driver.find_elements(By.CLASS_NAME,'el-checkbox__label')
            elements = driver.find_elements(By.CLASS_NAME, 'el-button')
            Active_account.css_text(model_content)
            Active_account.css_text(el_checkbox_label)
            Active_account.css_text(elements)
            pic_path = os.path.join(get_par_path(), 'shootpicture\\translation_usermanage\\')
            act_account_notranslation = pic_path + 'act_account_notranslation.png'
            Active_account.keyword_key(act_account_notranslation)
            allure.attach.file(act_account_notranslation, attachment_type=allure.attachment_type.PNG)
            Active_account.click_post_mail()
            Active_account.click_save_btn()
        with allure.step("完成激活账号"):
            actaccount_prompt_notranslation = pic_path + 'actaccount_prompt_notranslation.png'
            Active_account.keyword_key(actaccount_prompt_notranslation)
            allure.attach.file(actaccount_prompt_notranslation, attachment_type=allure.attachment_type.PNG)


