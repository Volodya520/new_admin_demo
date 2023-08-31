from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from new_admin_demo.pages.base_action import BaseAction
import yaml


# 登录页面信息定位
class Locator_Login(BaseAction):
    Elelocator_login= yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml',encoding='utf-8'))
    login_btn =  By.XPATH,Elelocator_login[0]['Locator_Login']['login_btn']
    login_name = By.ID, Elelocator_login[0]['Locator_Login']['login_name']
    login_pw = By.ID, Elelocator_login[0]['Locator_Login']['login_pw']
    login_submit = By.XPATH, Elelocator_login[0]['Locator_Login']['login_submit']

    # 点击方法
    def click_login_btn(self):
        self.click_i(self.login_btn)

    def click_login_submit(self):
        self.click_i(self.login_submit)

    # 输入方法
    def enter_keyword_login_name(self, text):
        self.input_things(self.login_name, text)

    def enter_keyword_login_pw(self, text):
        self.input_things(self.login_pw, text)


# 用户
# 邀请用户
class Locator_invite_user(BaseAction):
    Elelocator_invite_user = yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml', encoding='utf-8'))
    user = By.XPATH, Elelocator_invite_user[1]['User']
    inv_user_btn=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['inv_user_btn']
    mail_adress=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['mail_adress']
    regist_to=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['regist_to']
    select_regist_to=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['select_regist_to']
    role=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['role']
    select_role=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['select_role']
    next_step=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['next_step']
    inv_user_save_btn=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['inv_user_save_btn']
    invite_user_pop_closebtn=By.XPATH, Elelocator_invite_user[4]['Locator_invite_user']['invite_user_pop_closebtn']

# 输入方法
    def enter_keyword_mail_adress(self,text):
        self.input_things(self.mail_adress,text)

# 点击方法
    def click_invite_user_pop_closebtn(self):
        self.click_i(self.invite_user_pop_closebtn)

    def click_user(self):
        self.click_i(self.user)

    def click_inv_user(self):
        self.click_i(self.inv_user_btn)

    def click_regist_to(self):
        self.click_i(self.regist_to)

    def click_select_regist_to(self):
        self.click_i(self.select_regist_to)

    def click_role(self):
        self.click_i(self.role)

    def click_select_role(self):
        self.click_i(self.select_role)

    def click_next_step(self):
        self.click_i(self.next_step)

    def click_inv_user_save_btn(self):
        self.click_i(self.inv_user_save_btn)

# 删除邀请用户
class Locator_delete_invite_user(BaseAction):
    Elelocator_delete_invite_user= yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml', encoding='utf-8'))
    user = By.XPATH, Elelocator_delete_invite_user[1]['User']
    more_usermanage_option = By.XPATH, Elelocator_delete_invite_user[2]['Usermanage_moreoption']
    delete_btn=By.XPATH, Elelocator_delete_invite_user[9]['Locator_Delete_Createuser']['delete']
    del_mail = By.XPATH, Elelocator_delete_invite_user[9]['Locator_Delete_Createuser']['del_mail']
    del_input = By.XPATH, Elelocator_delete_invite_user[9]['Locator_Delete_Createuser']['del_input']
    del_btn = By.XPATH, Elelocator_delete_invite_user[9]['Locator_Delete_Createuser']['del_btn']


    # 输入方法
    def enter_keyword_del_input(self, text):
        self.input_things(self.del_input, text)

    # 点击方法
    def click_user(self):
        self.click_i(self.user)

    def click_btn_more_usermanage_option(self):
        self.click_i(self.more_usermanage_option)

    def click_btn_delete(self):
        self.click_i(self.delete_btn)

    def click_btn_del_mail(self):
        self.click_i(self.del_mail)

    def click_del_btn(self):
        self.click_i(self.del_btn)

# 创建账号定位
class Locator_Create_user(BaseAction):
    Elelocator_create_user=yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml',encoding='utf-8'))
    accountmanage = By.XPATH,Elelocator_create_user[5]['Locator_Create/Edit_user']['accountmanage']
    user_create = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['user_create']
    displayname = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['displayname']
    full_name = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['full_name']
    SIS_ID = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['SIS_ID']
    mail = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['create_mail']
    new_pw = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['new_pw']
    role = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['role']
    select_role = By.XPATH,Elelocator_create_user[5]['Locator_Create/Edit_user']['select_role']
    otherthing = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['otherthing']
    create_btn = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['create_btn']
    user_create_other = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['user_create_other']
    post_mail = By.XPATH, Elelocator_create_user[5]['Locator_Create/Edit_user']['post_mail']

    # 输入方法
    def enter_keyword_create_full_name(self, text):
        self.input_things(self.full_name, text)

    def enter_keyword_create_displayname(self, text):
        self.input_things(self.displayname,text)

    def enter_keyword_create_SIS_ID(self, text):
        self.input_things(self.SIS_ID,text)

    def enter_keywords_create_mail(self, text):
        self.input_things(self.mail,text)

    def enter_keyword_create_new_pw(self, text):
        self.input_things(self.new_pw,text)

    # 点击方法
    def click_accountmanage(self):
        self.click_i(self.accountmanage)

    def click_user_create(self):
        self.click_i(self.user_create)

    def click_create_user_role(self):
        self.click_i(self.role)

    def click_create_select_role(self):
        self.click_i(self.select_role)

    def click_create_otherthing(self):
        self.click_i(self.otherthing)

    def click_create_btn(self):
        self.click_i(self.create_btn)

# 编辑账号定位
class Locator_Edit_Createuser(BaseAction):
    Elelocator_Edit_Createuser=yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml',encoding='utf-8'))
    user=By.XPATH,Elelocator_Edit_Createuser[1]['User']
    full_name = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['full_name']
    displayname = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['displayname']
    SIS_ID = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['SIS_ID']
    mail = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['edit_mail']
    more_usermanage_option = By.XPATH, Elelocator_Edit_Createuser[2]['Usermanage_moreoption']
    edit_user = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['edit_user']
    edit_mailbtn = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['edit_mailbtn']
    edit_post_mail = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['edit_post_mail']
    edit_save_btn = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['edit_save_btn']
    post_mail = By.XPATH, Elelocator_Edit_Createuser[5]['Locator_Create/Edit_user']['post_mail']

    # 输入方法
    def enter_keyword_fullname(self,text):
        self.input_things(self.full_name,text)

    def enter_keyword_displayname(self,text):
        self.input_things(self.displayname,text)

    def enter_keyword_SIS_ID(self,text):
        self.input_things(self.SIS_ID,text)

    def enter_keyword_mail(self,text):
        self.input_things(self.mail,text)

    # 点击方法
    def click_user(self):
        self.click_i(self.user)

    def click_more_usermanage_option(self):
        self.click_i(self.more_usermanage_option)

    def click_btn_edit_user(self):
        self.click_i(self.edit_user)

    def click_btn_edit_mail(self):
        self.click_i(self.edit_mailbtn)

    def click_btnpost_mail(self):
        self.click_i(self.edit_post_mail)

    def click_edit_save_btn(self):
        self.click_i(self.edit_save_btn)

#修改密码
class Locator_Edit_Pw(BaseAction):
    EleLocator_Edit_Pw = yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml', encoding='utf-8'))
    user=By.XPATH, EleLocator_Edit_Pw[1]['User']
    more_usermanage_option = By.XPATH, EleLocator_Edit_Pw[2]['Usermanage_moreoption']
    edit_pw=By.XPATH, EleLocator_Edit_Pw[6]['Locator_Edit_pw']['edit_pw']
    new_pw=By.XPATH, EleLocator_Edit_Pw[6]['Locator_Edit_pw']['new_pw']
    confirm_pw=By.XPATH, EleLocator_Edit_Pw[6]['Locator_Edit_pw']['confirm_pw']
    save_btn=By.XPATH, EleLocator_Edit_Pw[6]['Locator_Edit_pw']['save_btn']
    edit_pw_suf_pop_closebtn=By.XPATH, EleLocator_Edit_Pw[6]['Locator_Edit_pw']['edit_pw_sufpop_closebtn']
# 输入方法
    def enter_keyword_new_pw(self,text):
        self.input_things(self.new_pw,text)

    def enter_keyword_confirm_pw(self,text):
        self.input_things(self.confirm_pw,text)

# 点击方法
    def click_user(self):
        self.click_i(self.user)

    def click_edit_pw_suf_pop(self):
        self.click_i(self.edit_pw_suf_pop_closebtn)

    def click_btn_more_usermanage_option(self):
        self.click_i(self.more_usermanage_option)

    def click_edit_pw(self):
        self.click_i(self.edit_pw)

    def click_save_btn(self):
        self.click_i(self.save_btn)

# 停用账号
class Locator_disable_account(BaseAction):
    EleLocator_disable_account = yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml', encoding='utf-8'))
    user=By.XPATH, EleLocator_disable_account[1]['User']
    more_usermanage_option = By.XPATH, EleLocator_disable_account[2]['Usermanage_moreoption']
    dis_account = By.XPATH, EleLocator_disable_account[7]['Locator_disable_account']['dis_account']
    post_mail=By.XPATH, EleLocator_disable_account[7]['Locator_disable_account']['post_mail']
    save_btn=By.XPATH, EleLocator_disable_account[7]['Locator_disable_account']['save_btn']

    def click_user(self):
        self.click_i(self.user)

    def click_btn_more_usermanage_option(self):
        self.click_i(self.more_usermanage_option)

    def click_dis_account(self):
        self.click_i(self.dis_account)

    def click_post_mail(self):
        self.click_i(self.post_mail)

    def click_save_btn(self):
        self.click_i(self.save_btn)

# 激活账号
class Locator_active_account(BaseAction):
    EleLocator_active_account = yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml', encoding='utf-8'))
    user = By.XPATH, EleLocator_active_account[1]['User']
    more_usermanage_option = By.XPATH, EleLocator_active_account[2]['Usermanage_moreoption']
    act_account=By.XPATH, EleLocator_active_account[8]['Locator_active_account']['act_account']
    post_mail = By.XPATH, EleLocator_active_account[8]['Locator_active_account']['post_mail']
    save_btn = By.XPATH, EleLocator_active_account[8]['Locator_active_account']['save_btn']

# 点击方法
    def click_user(self):
        self.click_i(self.user)

    def click_btn_more_usermanage_option(self):
        self.click_i(self.more_usermanage_option)

    def click_act_account(self):
        self.click_i(self.act_account)

    def click_post_mail(self):
        self.click_i(self.post_mail)

    def click_save_btn(self):
        self.click_i(self.save_btn)

# 删除用户定位
class Locator_Delete_Createuser(BaseAction):
    EleLocator_Delete_Createuser = yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml', encoding='utf-8'))
    account_manage = By.XPATH, EleLocator_Delete_Createuser[3]['account_manage']
    more_usermanage_option = By.XPATH, EleLocator_Delete_Createuser[2]['Usermanage_moreoption']
    delete = By.XPATH, EleLocator_Delete_Createuser[9]['Locator_Delete_Createuser']['delete']
    del_mail = By.XPATH, EleLocator_Delete_Createuser[9]['Locator_Delete_Createuser']['del_mail']
    del_input = By.XPATH, EleLocator_Delete_Createuser[9]['Locator_Delete_Createuser']['del_input']
    del_btn = By.XPATH, EleLocator_Delete_Createuser[9]['Locator_Delete_Createuser']['del_btn']

    # 输入方法
    def enter_keyword_del_input(self, text):
        self.input_things(self.del_input, text)

    # 点击方法
    def click_account_manage(self):
        self.click_i(self.account_manage)

    def click_btn_more_usermanage_option(self):
        self.click_i(self.more_usermanage_option)

    def click_btn_delete(self):
        self.click_i(self.delete)

    def click_btn_del_mail(self):
        self.click_i(self.del_mail)

    def click_del_btn(self):
        self.click_i(self.del_btn)


# 注册账号
class Locator_reg_to_account(BaseAction):
    EleLocator_reg_to_account = yaml.safe_load(open('../datafile/Ele_locator/userregister_locator.yaml',encoding='utf-8'))
    user = By.XPATH, EleLocator_reg_to_account[1]['User']
    registmanage = By.XPATH,EleLocator_reg_to_account[2]['registmanage']
    regto_account = By.XPATH, EleLocator_reg_to_account[4]['Locator_reg_to_account']['regto_account']
    bymail_list=By.XPATH,EleLocator_reg_to_account[4]['Locator_reg_to_account']['bymail_account']
    regist_to = By.XPATH, "(//input[@placeholder='请选择'])[2]"
    select_regist_to = By.XPATH, EleLocator_reg_to_account[4]['Locator_reg_to_account']['select_regist_to']
    role=By.XPATH,EleLocator_reg_to_account[3]['role']
    select_role1 = By.XPATH, EleLocator_reg_to_account[4]['Locator_reg_to_account']['select_role1']
    select_role2=By.XPATH,EleLocator_reg_to_account[4]['Locator_reg_to_account']['select_role2']
    next_btn=By.XPATH,EleLocator_reg_to_account[4]['Locator_reg_to_account']['next_btn']
    regto_account_save_btn = By.XPATH, EleLocator_reg_to_account[4]['Locator_reg_to_account']['regto_account_save_btn']
    regto_account_pop_closebtn=By.XPATH,EleLocator_reg_to_account[4]['Locator_reg_to_account']['regto_account_pop_closebtn']


#     输入方法
    def enter_keyword_bymail_list(self,text):
        self.input_things(self.bymail_list,text)

    # 点击方法
    def click_regto_account_pop_closebtn(self):
        self.click_i(self.regto_account_pop_closebtn)

    def click_user(self):
        self.click_i(self.user)

    def click_registmanage(self):
        self.click_i(self.registmanage)

    def click_regto_account(self):
        self.click_i(self.regto_account)

    def click_regist_to(self):
        self.click_i(self.regist_to)

    def click_select_regist_to(self):
        self.click_i(self.select_regist_to)

    def click_role(self):
        self.click_i(self.role)

    def click_select_role1(self):
        self.click_i(self.select_role1)

    def click_select_role2(self):
        self.click_i(self.select_role2)

    def click_next_btn(self):
        self.click_i(self.next_btn)

    def click_regto_account_save_btn(self):
        self.click_i(self.regto_account_save_btn)

# 编辑注册账号
class Locator_edit_reg_to_account(BaseAction):
    Elelocator_edit_regto_account=yaml.safe_load(open('../datafile/Ele_locator/userregister_locator.yaml',encoding='utf-8'))
    user = By.XPATH, Elelocator_edit_regto_account[1]['User']
    registmanage = By.XPATH, Elelocator_edit_regto_account[2]['registmanage']
    change_org=By.XPATH,Elelocator_edit_regto_account[6]['Locator_edit/remove_reg_to_account']['change_org']
    select_change_org=By.XPATH,Elelocator_edit_regto_account[6]['Locator_edit/remove_reg_to_account']['select_change_org']
    more_option=By.XPATH,Elelocator_edit_regto_account[6]['Locator_edit/remove_reg_to_account']['more_option']
    edit_regto_account=By.XPATH,Elelocator_edit_regto_account[6]['Locator_edit/remove_reg_to_account']['edit_regto_account']
    close_role=By.XPATH,Elelocator_edit_regto_account[6]['Locator_edit/remove_reg_to_account']['close_role']
    edit_save_btn=By.XPATH,Elelocator_edit_regto_account[6]['Locator_edit/remove_reg_to_account']['edit_save_btn']
    edit_regto_account_pop_closebtn=By.XPATH,Elelocator_edit_regto_account[6]['Locator_edit/remove_reg_to_account']['edit_regto_account_pop_closebtn']
    search_account=By.XPATH,Elelocator_edit_regto_account[6]['Locator_edit/remove_reg_to_account']['search_account']


    # 输入方法
    def enter_keyword_search_account(self, text):
        self.input_things(self.search_account, text)

# 点击方法
    def click_edit_regto_account_pop_closebtn(self):
        self.click_i(self.edit_regto_account_pop_closebtn)

    def click_user(self):
        self.click_i(self.user)

    def click_registmanage(self):
        self.click_i(self.registmanage)

    def click_change_org(self):
        self.click_i(self.change_org)

    def click_select_change_org(self):
        self.click_i(self.select_change_org)

    def click_more_option(self):
        self.click_i(self.more_option)

    def click_edit_regto_account(self):
        self.click_i(self.edit_regto_account)

    def click_close_role(self):
        self.click_i(self.close_role)

    def click_edit_save_btn(self):
        self.click_i(self.edit_save_btn)


# 移除注册账号
class Locator_remove_regto_account(BaseAction):
    Elelocator_remove_regto_account = yaml.safe_load(open('../datafile/Ele_locator/userregister_locator.yaml', encoding='utf-8'))
    user = By.XPATH, Elelocator_remove_regto_account[1]['User']
    registmanage = By.XPATH, Elelocator_remove_regto_account[2]['registmanage']
    change_org= By.XPATH,Elelocator_remove_regto_account[6]['Locator_edit/remove_reg_to_account']['change_org']
    select_change_org= Elelocator_remove_regto_account[6]['Locator_edit/remove_reg_to_account']['select_change_org']
    more_option = By.XPATH,Elelocator_remove_regto_account[6]['Locator_edit/remove_reg_to_account']['more_option']
    remove_regto_account=By.XPATH,Elelocator_remove_regto_account[6]['Locator_edit/remove_reg_to_account']['remove_regto_account']
    post_mail=By.XPATH,Elelocator_remove_regto_account[6]['Locator_edit/remove_reg_to_account']['post_mail']
    remove_save_btn=By.XPATH,Elelocator_remove_regto_account[6]['Locator_edit/remove_reg_to_account']['remove_save_btn']
    search_account = By.XPATH, Elelocator_remove_regto_account[6]['Locator_edit/remove_reg_to_account']['search_account']

    # 点击方法
    def click_user(self):
        self.click_i(self.user)

    def click_registmanage(self):
        self.click_i(self.registmanage)

    def click_change_org(self):
        self.click_i(self.change_org)

    def click_select_change_org(self):
        self.click_i(self.select_change_org)

    def click_more_option(self):
        self.click_i(self.more_option)

    def click_remove_regto_account(self):
        self.click_i(self.remove_regto_account)

    def click_post_mail(self):
        self.click_i(self.post_mail)

    def click_remove_save_btn(self):
        self.click_i(self.remove_save_btn)

 # 输入方法
    def enter_keyword_search_account(self,text):
        self.input_things(self.search_account,text)




#  通过账号注册
class Locator_regto_byaccount(BaseAction):
    Elelocator_regto_byaccount = yaml.safe_load(open('../datafile/Ele_locator/userregister_locator.yaml', encoding='utf-8'))
    user = By.XPATH, Elelocator_regto_byaccount[1]['User']
    registmanage = By.XPATH, Elelocator_regto_byaccount[2]['registmanage']
    regto_account = By.XPATH, Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['regto_account']
    by_account=By.XPATH,Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['by_account']
    exist_account=By.XPATH,Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['exist_account']
    search_user=By.XPATH,Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['search_user']
    confirm_sear_result=By.XPATH,Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['confirm_sear_result']
    choose_user=By.XPATH,Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['choose_user']
    confirm_btn=By.XPATH,Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['confirm_btn']
    role = By.XPATH,Elelocator_regto_byaccount[3]['role']
    select_role1 = By.XPATH,Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['select_role1']
    select_role2 = By.XPATH, Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['select_role2']
    next_btn = By.XPATH,Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['next_btn']
    regto_account_save_btn = By.XPATH, Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['regto_account_save_btn']
    regto_account_pop_closebtn = By.XPATH, Elelocator_regto_byaccount[5]['Locator_regto_byaccount']['regto_account_pop_closebtn']


#     输入方法
    def enter_keyword_search_user(self,text):
        self.input_things(self.search_user,text)

#     点击方法
    def click_confirm_sear_result(self):
        self.click_i(self.confirm_sear_result)

    def click_regto_account_pop_closebtn(self):
        self.click_i(self.regto_account_pop_closebtn)

    def click_user(self):
        self.click_i(self.user)

    def click_registmanage(self):
        self.click_i(self.registmanage)

    def click_regto_account(self):
        self.click_i(self.regto_account)

    def click_by_account(self):
        self.click_i(self.by_account)

    def click_exist_account(self):
        self.click_i(self.exist_account)

    def click_choose_user(self):
        self.click_i(self.choose_user)

    def click_confirm_btn(self):
        self.click_i(self.confirm_btn)

    def click_role(self):
        self.click_i(self.role)

    def click_select_role1(self):
        self.click_i(self.select_role1)

    def click_select_role2(self):
        self.click_i(self.select_role2)

    def click_next_btn(self):
        self.click_i(self.next_btn)

    def click_regto_account_save_btn(self):
        self.click_i(self.regto_account_save_btn)


class UsermanageResultPage(BaseAction):
    # 没什么属性
    # 方法: 返回要 验证文本
    Elelocator_userregistResultPage = yaml.safe_load(open('../datafile/Ele_locator/userregister_locator.yaml', encoding='utf-8'))
    Elelocator_usermanageResult_Page=yaml.safe_load(open('../datafile/Ele_locator/usermanage_locator.yaml',encoding='utf-8'))
    user_create_other = By.XPATH, Elelocator_usermanageResult_Page[10]['UsermanageResultPage']['user_create_other']
    create_acount_page = By.XPATH, Elelocator_usermanageResult_Page[10]['UsermanageResultPage']['create_acount_page']
    edit_acount_page=By.XPATH,Elelocator_usermanageResult_Page[10]['UsermanageResultPage']['edit_acount_page']
    delete_acount_page=By.XPATH,Elelocator_usermanageResult_Page[10]['UsermanageResultPage']['delete_acount_page']
    edit_pw_suf_pop=By.XPATH,Elelocator_usermanageResult_Page[10]['UsermanageResultPage']['edit_pw_suf_pop']
    account_state = By.XPATH,Elelocator_usermanageResult_Page[10]['UsermanageResultPage']['account_state']
    invite_user_pop=By.XPATH,Elelocator_usermanageResult_Page[10]['UsermanageResultPage']['invite_user_pop']
    regto_account_pop=By.XPATH,Elelocator_userregistResultPage[7]['UserregistReusultPage']['regto_account_pop']
    edit_regto_account_pop=By.XPATH,Elelocator_userregistResultPage[7]['UserregistReusultPage']['edit_regto_account_pop']
    remove_regto_acount=By.XPATH,Elelocator_userregistResultPage[7]['UserregistReusultPage']['remove_regto_acount']


    # 账号管理验证页面
    def get_accountmanage(self):
        ele=self.driver.find_element(*self.user_create_other)
        return ele.text

    # 成功修改密码窗口验证结果
    def get_edit_pw_suf_pop(self):
        ele=self.driver.find_element(*self.edit_pw_suf_pop)
        return ele.text

    # 停用/激活: 账号验证结果
    def act_dis_account_ele(self):
        ele=self.driver.find_element(*self.account_state)
        return ele.text

    # 邀请用户验证结果
    def get_invite_user(self):
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(self.invite_user_pop))
        ele=self.driver.find_element(*self.invite_user_pop)
        return ele.text

    # 注册账号验证结果
    def get_regto_account(self):
        ele=self.driver.find_element(*self.regto_account_pop)
        return ele.text

    # 编辑注册账号验证结果
    def get_edit_regto_account(self):
        ele=self.driver.find_element(*self.edit_regto_account_pop)
        return ele.text

    # 移除注册账号验证结果
    def get_remove_regto_account(self):
        ele = self.driver.find_element(*self.remove_regto_acount)
        return ele.text

