import os
import time

import yaml
import pytest
from new_admin_demo.Utils.get_path import get_par_path
from new_admin_demo.Utils.log import conf
from new_admin_demo.Utils.read_yml import get_yaml_data
from new_admin_demo.pages.page_newadmin import *
import allure


class TestClass_usermanage(object):
    @allure.step('从配置文件中读取登陆数据')
    @pytest.fixture()
    def login_data(self):
        self.log=conf.logcon()
        self.log.info(("read_config.yaml"))
        yaml_path = os.path.join(get_par_path(), "config/user_manage_config.yaml")
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

    # 用户模块
    # # #1. 账号管理
    # 邀请用户
    @allure.story('账号管理')
    @allure.title('邀请用户')
    @pytest.mark.parametrize("get_data", yaml.safe_load(open('../datafile/test_datatext/test__invite_user.yaml', encoding='utf-8')))
    # @pytest.mark.parametrize("keyword",['1921507475@qq.com,12345678'])
    def test_invite_user(self,driver,get_data):
        keyword=get_data["case"]
        input=keyword['keyword']
        with allure.step('初始化邀请用户页'):
            Invite_user=Locator_invite_user(driver)
        Invite_user.click_user()
        Invite_user.click_inv_user()
        with allure.step('输入邮件地址'):
            Invite_user.enter_keyword_mail_adress(input)
        with allure.step('注册到子机构'):
            Invite_user.click_regist_to()
            Invite_user.click_select_regist_to()
        with allure.step('选择角色'):
            Invite_user.click_role()
            Invite_user.click_select_role()
        with allure.step('完成邀请用户操作'):
            Invite_user.click_next_step()
            Invite_user.click_inv_user_save_btn()
        WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located(UsermanageResultPage.invite_user_pop))
        with allure.step('初始化结果页面'):
            result_page=UsermanageResultPage(driver)
        with allure.step('判断1921507475@qq.com邮箱否邀请成功并截图'):
            assert '1921507475@qq.com' in result_page.get_invite_user()
            pic_path=os.path.join(get_par_path(), 'shootpicture\\')
            pic_name=pic_path+'inviteuser.png'
            result_page.save_picture(pic_name)
            allure.attach.file(pic_name,attachment_type=allure.attachment_type.PNG)


    # # 删除账号*****
    @allure.story('账号管理')
    @allure.title('删除待激活的账号')
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_delete_invite_user.yaml', encoding='utf-8')))
    # @pytest.mark.parametrize('keyword',['删除账号'])
    def test_delete_invite_user(self,driver,get_data):
        keyword = get_data["case"]
        input = keyword['keyword']
        # with allure.step('初始化删除账号'):
        Delete_invite_user=Locator_delete_invite_user(driver)
        Invite_user = Locator_invite_user(driver)
        with allure.step('进入用户页面删除账号'):
            Invite_user.click_invite_user_pop_closebtn()
            # Delete_invite_user.click_user()
            Delete_invite_user.click_btn_more_usermanage_option()
            time.sleep(2)
            Delete_invite_user.click_btn_delete()
        with allure.step('删除账号的弹窗'):
            Delete_invite_user.click_btn_del_mail()
            Delete_invite_user.enter_keyword_del_input(input)
            Delete_invite_user.click_del_btn()
        # with allure.step('初始化结果页面'):
        result_page = UsermanageResultPage(driver)
        WebDriverWait(driver, 10, 1).until(EC.invisibility_of_element_located(UsermanageResultPage.delete_acount_page))
        with allure.step('判断1921507475@qq.com的邮箱是否删除成功并截图'):
            assert '1921507475@qq.com' not in result_page.get_accountmanage()
            pic_path=os.path.join(get_par_path(), 'shootpicture\\')
            pic_name=pic_path+'delete_inviteuser.png'
            result_page.save_picture(pic_name)
            allure.attach.file(pic_name,attachment_type=allure.attachment_type.PNG)


    # 创建账号*****
    @allure.story('账号管理')
    @allure.title("创建账号")
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_create_user.yaml', encoding='utf-8')))
    # @pytest.mark.parametrize("fullname,displayname,SIS_ID,mail,new_pw",[('202322','202322','2023115','1921507475@qq.com','wenhua123')])
    def test_create_user(self,driver,get_data):
        keyword=get_data['case1']
        fullname=keyword['fullname']
        displayname=keyword['displayname']
        SIS_ID=keyword['SIS_ID']
        mail=keyword['mail']
        new_pw=keyword['new_pw']
        # with allure.step('初始化创建账号弹窗'):
        Create_user=Locator_Create_user(driver)
        with allure.step('点击按钮跳出创建弹窗'):
            Create_user.click_accountmanage()
            Create_user.click_user_create()
        with allure.step('输入必填文字信息'):
            Create_user.enter_keyword_create_full_name(fullname)
            Create_user.enter_keyword_create_displayname(displayname)
            Create_user.enter_keyword_create_SIS_ID(SIS_ID)
            Create_user.enter_keywords_create_mail(mail)
            Create_user.enter_keyword_create_new_pw(new_pw)
        with allure.step('选择角色'):
            time.sleep(2)
            Create_user.click_create_user_role()
            time.sleep(2)
            Create_user.click_create_select_role()
        with allure.step('机构默认注册到：本机构'):
            Create_user.click_create_otherthing()
            Create_user.click_create_btn()
        # with allure.step("初始化结果页面"):
        result_page=UsermanageResultPage(driver)
        WebDriverWait(driver, 10, 1).until(EC.invisibility_of_element_located(UsermanageResultPage.create_acount_page))
        with allure.step('判断1921507475@qq.com的邮箱是创建成功并截图'):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'create_user.png'
            result_page.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert '1921507475@qq.com' in result_page.get_accountmanage()



    # 编辑账号
    @allure.story('账号管理')
    @allure.title("编辑账号")
    # @pytest.mark.parametrize('fullname,displayname,SIS_ID,mail',[('202322','202322','202322','linghuidu15@163.com')])
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_edit_user.yaml', encoding='utf-8')))
    def test_edit_user(self,driver,get_data):
        keyword=get_data['case']
        fullname=keyword['fullname']
        displayname=keyword['displayname']
        SIS_ID=keyword['SIS_ID']
        mail=keyword['mail']
        # with allure.step("初始化编辑页面"):
        Edit_user=Locator_Edit_Createuser(driver)
        with allure.step("进入编辑页面"):
            Edit_user.click_user()
            Edit_user.click_more_usermanage_option()
            time.sleep(2)
            Edit_user.click_btn_edit_user()
        with allure.step("输入修改的信息文本"):
            Edit_user.enter_keyword_fullname(fullname)
            Edit_user.enter_keyword_displayname(displayname)
            Edit_user.enter_keyword_SIS_ID(SIS_ID)
        with allure.step('修改邮箱为linghuidu15@163.com'):
            Edit_user.click_btn_edit_mail()
            Edit_user.enter_keyword_mail(mail)
        with allure.step("勾选邮件提醒"):
            Edit_user.click_btnpost_mail()
            Edit_user.click_edit_save_btn()
        # with allure.step("初始化结果页面"):
        result_page=UsermanageResultPage(driver)
        WebDriverWait(driver, 10, 1).until(EC.invisibility_of_element_located(UsermanageResultPage.edit_acount_page))
        with allure.step('判断linghuidu15@163.com的邮箱是否修改成功并截图'):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'edit_create_user.png'
            result_page.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert 'linghuidu15@163.com' in result_page.get_accountmanage()


    # 修改密码
    @allure.story('账号管理')
    @allure.title("修改密码")
    @pytest.mark.parametrize('get_data', yaml.safe_load(open('../datafile/test_datatext/test_edit_pw.yaml', encoding='utf-8')))
    # @pytest.mark.parametrize('new_pw,confirm_pw,expect_result',[('dulinghui123','dulinghui123','密码已修改')])
    def test_edit_pw(self,driver,get_data):
        keyword=get_data['case']
        new_pw=keyword['new_pw']
        confirm_pw=keyword['confirm_pw']
        # with allure.step("初始化登录页面")
        Edit_pw=Locator_Edit_Pw(driver)
        with allure.step("进入修改密码页面"):
            Edit_pw.click_user()
            Edit_pw.click_btn_more_usermanage_option()
            time.sleep(2)
            Edit_pw.click_edit_pw()
        with allure.step("输入新密码：123456du"):
            Edit_pw.enter_keyword_new_pw(new_pw)
        with allure.step("确认密码"):
            Edit_pw.enter_keyword_confirm_pw(confirm_pw)
        with allure.step("保存"):
            Edit_pw.click_save_btn()
        time.sleep(2)
        # with allure.step("初始化结果页面"):
        resultpage = UsermanageResultPage(driver)
        with allure.step('判断密码是否修改成功并截图'):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'edit_pw.png'
            resultpage.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert '密码已修改' in resultpage.get_edit_pw_suf_pop()


    # 停用
    @allure.story('账号管理')
    @allure.title("停用账号")
    def test_disable_account(self,driver):
        # with allure.step("初始化停用账号界面"):
        Dis_account= Locator_disable_account(driver)
        with allure.step('进入停用账号页面'):
            Edit_pw = Locator_Edit_Pw(driver)
            Edit_pw.click_edit_pw_suf_pop()
            Dis_account.click_user()
            Dis_account.click_btn_more_usermanage_option()
            time.sleep(2)
            Dis_account.click_dis_account()
        with allure.step("勾选邮件提醒"):
            Dis_account.click_post_mail()
        with allure.step("保存按钮"):
            Dis_account.click_save_btn()
            time.sleep(2)
        # with allure.step("初始化结果页面"):
        resultpage=UsermanageResultPage(driver)
        with allure.step('判断账号是否停用成功并截图'):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'disable_user.png'
            resultpage.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert '已停用' in resultpage.act_dis_account_ele()


    # 激活
    @allure.story('账号管理')
    @allure.title("激活账号")
    def test_active_account(self,driver):
        # with allure.step("初始化激活账号页面")
        Active_account=Locator_active_account(driver)
        with allure.step('进入停用账号页面'):
            Active_account.click_user()
            Active_account.click_btn_more_usermanage_option()
            time.sleep(2)
            Active_account.click_act_account()
        with allure.step("勾选邮件通知"):
            Active_account.click_post_mail()
            Active_account.click_save_btn()
        time.sleep(2)
        # with allure.step("初始化结果页面"):
        resultpage = UsermanageResultPage(driver)
        with allure.step("判断账号是否激活成功并截图"):
            pic_path = os.path.join(get_par_path(), 'shootpicture\\')
            pic_name = pic_path + 'active_user.png'
            resultpage.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
            assert '激活' in resultpage.act_dis_account_ele()




