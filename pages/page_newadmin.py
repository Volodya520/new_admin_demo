from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from new_admin_demo.pages.base_action import BaseAction

# 登录页面信息定位
class Locator_Login(BaseAction):
    login_btn = By.XPATH, '/html/body/div[1]/div/div/header/nav/div/button'
    login_name = By.ID, 'userLoginName'
    login_pw = By.ID, "userPassword"
    login_submit = By.XPATH, '//*[@id="loginForm"]/button'

    # 点击方法
    def click_btn_login_btn(self):
        self.click_i(self.login_btn)

    def click_btn_login_submit(self):
        self.click_i(self.login_submit)

    # 输入方法
    def enter_keyword_login_name(self, text):
        self.input_things(self.login_name, text)

    def enter_keyword_login_pw(self, text):
        self.input_things(self.login_pw, text)

# 退出登录的页面定位：
class Locator_Logout_user(BaseAction):
    mine=By.XPATH,'/html/body/div[1]/div/div/header/nav/div/div[2]/div'
    logout=By.XPATH,'/html/body/div[1]/div/div/header/nav/div/div[2]/ul/li[2]'

    # 点击事件
    def click_mine(self):
        self.click_i(self.mine)

    def click_logout(self):
        self.click_i(self.logout)
# 用户
# 创建账号定位
class Locator_Create_user(BaseAction):
    accountmanage = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    user_create = By.XPATH, '//*[@id="pane-accountManager"]/div/div[1]/form/div[3]/button[2]'
    displayname = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div/div/div/input'
    full_name = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[1]/div/div/input'
    SIS_ID = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div/input'
    mail = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[3]/div/div/input'
    new_pw = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[4]/div/div/input'
    role = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[6]/div/div/div[2]/span'
    # select_role = By.XPATH,"(//li[@class='el-select-dropdown__item'])[4]"
    select_role = By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    otherthing = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]'
    create_btn = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[3]/div/button[2]'
    user_create_other = By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div[2]'
    post_mail = By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div[2]'

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
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    user_create = By.XPATH, '//*[@id="pane-accountManager"]/div/div[1]/form/div[3]/button[2]'
    full_name = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[1]/div/div/input'
    displayname = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div/div/div/input'
    SIS_ID = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div/input'
    mail = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[3]/div/div/input'
    more_usermanage_option = By.XPATH, '/html/body/div/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/div'
    edit_user = By.XPATH, '/html/body/ul/li[1]'
    edit_mail = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/div[3]/div/span'
    edit_post_mail = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[2]/form/label/span[1]'
    edit_save_btn = By.XPATH, '//*[@id="pane-accountManager"]/div/div[3]/div/div[3]/div/button[2]'
    post_mail = By.XPATH, '//*[@id="app"]/div/div[3]/section/div/div[2]/div[2]'
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
        self.click_i(self.edit_mail)

    def click_btnpost_mail(self):
        self.click_i(self.edit_post_mail)

    def click_edit_save_btn(self):
        self.click_i(self.edit_save_btn)

#修改密码
class Locator_Edit_Pw(BaseAction):
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    more_usermanage_option = By.XPATH, '/html/body/div/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/div'
    edit_pw=By.XPATH,'/html/body/ul/li[2]'
    new_pw=By.XPATH,'//*[@id="pane-accountManager"]/div/div[4]/div/div[2]/div/div[2]/form/div[1]/div/div[1]/input'
    confirm_pw=By.XPATH,'//*[@id="pane-accountManager"]/div/div[4]/div/div[2]/div/div[2]/form/div[2]/div/div/input'
    save_btn=By.XPATH,'//*[@id="pane-accountManager"]/div/div[4]/div/div[3]/div/div[2]/button[2]'
    edit_pw_suf_pop_closebtn=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[4]/div/div[3]/div/div[3]/button'

# 输入方法
    def enter_keyword_new_pw(self,text):
        self.input_things(self.new_pw,text)

    def enter_keyword_confirm_pw(self,text):
        self.input_things(self.confirm_pw,text)

# 点击方法
    def click_edit_pw_suf_pop(self):
        self.click_i(self.edit_pw_suf_pop_closebtn)

    def click_user(self):
        self.click_i(self.user)

    def click_btn_more_usermanage_option(self):
        self.click_i(self.more_usermanage_option)

    def click_edit_pw(self):
        self.click_i(self.edit_pw)

    def click_save_btn(self):
        self.click_i(self.save_btn)

# 停用账号
class Locator_disable_account(BaseAction):
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    more_usermanage_option = By.XPATH, '/html/body/div/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/div'
    dis_account = By.XPATH,'/html/body/ul/li[3]'
    post_mail=By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/label/span[1]'
    save_btn=By.XPATH,'/html/body/div[3]/div/div[3]/div/button[2]'

    # 点击方法
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
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    more_usermanage_option = By.XPATH, '/html/body/div/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/div'
    act_account=By.XPATH,'/html/body/ul/li[3]'
    post_mail = By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/label/span[1]'
    save_btn = By.XPATH, '/html/body/div[3]/div/div[3]/div/button[2]'
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
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    account_manage = By.XPATH, '/html/body/div[1]/div/div[3]/section/div/div[2]/div[1]/div/div/div/div[2]'
    more_usermanage_option = By.XPATH, '/html/body/div/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div'
    delete = By.XPATH, "/html/body/ul/li[4]"
    del_mail = By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[1]/label/span[1]/span'
    del_input = By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/input'
    del_btn = By.XPATH, "//div[@class='el-dialog__wrapper actionConfirmDialog']//button[2]//span[1]"

    # 输入方法
    def enter_keyword_del_input(self, text):
        self.input_things(self.del_input, text)

    # 点击方法
    def click_user(self):
        self.click_i(self.user)

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

# 邀请用户
class Locator_invite_user(BaseAction):
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    inv_user_btn=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[1]/form/div[3]/button[1]'
    mail_adress=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div[2]/div/div[1]/form/div[1]/div/div/textarea'
    regist_to=By.XPATH,'//*[@id="pane-accountManager"]/div/div[3]/div/div/div[2]/div/div[1]/form/div[2]/div/div/div[1]'
    select_regist_to=By.XPATH,'/html/body/div[3]/div[1]/div/div[1]/ul/li[5]/label'
    role=By.XPATH,'//*[@id="pane-accountManager"]/div/div[3]/div/div/div[2]/div/div[1]/form/div[3]/div/div[1]/div[2]/span'
    select_role=By.XPATH,"(//li[@class='el-select-dropdown__item'])[4]"
    next_step=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div[3]/div/div[1]/button[2]'
    inv_user_save_btn=By.XPATH,'//*[@id="pane-accountManager"]/div/div[3]/div/div/div[3]/div/div[2]/button[3]'
    invite_user_pop_closebtn=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div[3]/div/div[3]/button'

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
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    more_usermanage_option = By.XPATH, '//*[@id="pane-accountManager"]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div'

    delete_btn=By.XPATH,'/html/body/ul/li[4]'
    del_mail = By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[1]/label/span[1]/span'
    del_input = By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]/input'
    del_btn = By.XPATH, "//div[@class='el-dialog__wrapper actionConfirmDialog']//button[2]//span[1]"


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

# 注册账号
class Locator_reg_to_account(BaseAction):
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    registmanage = By.XPATH,'/html/body/div/div/div[3]/section/div/div[2]/div[1]/div/div/div/div[3]'
    regto_account = By.XPATH,'//*[@id="pane-registerManager"]/div/div[1]/form/div[4]/button'
    bymail_list=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[1]/form/div[2]/div/div[1]/textarea'
    regist_to = By.XPATH, '//*[@id="pane-registerManager"]/div/div[3]/div/div/div[2]/div/div[1]/form/div[3]/div/div/div[1]/input'
    select_regist_to = By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/ul/li[5]/label/span[1]/span'
    role=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[1]/form/div[4]/div/div/div[2]/input'
    select_role1 = By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    select_role2=By.XPATH,"/html/body/div[4]/div[1]/div[1]/ul/li[6]"
    next_btn=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div[1]/button[2]'
    regto_account_save_btn = By.XPATH, '/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div[2]/button[3]'
    regto_account_pop_closebtn=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div[3]/button'

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
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    registmanage = By.XPATH, '/html/body/div/div/div[3]/section/div/div[2]/div[1]/div/div/div/div[3]'
    change_org=By.XPATH,'//*[@id="pane-registerManager"]/div/div[1]/form/div[2]/div/div/div[1]/input'
    select_change_org=By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[5]/label/span[1]/span'
    more_option=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[9]/td[5]/div/div/div'
    edit_regto_account=By.XPATH,'/html/body/ul/li[1]'
    close_role=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[2]/div/form/div[2]/div/div/div[1]/span/span[1]/i'
    edit_save_btn=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[4]/div/div[3]/div/div[2]/button[2]'
    edit_regto_account_pop_closebtn=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[4]/div/div[3]/div/div[3]/button'

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
    more_option = By.XPATH, '/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[9]/td[5]/div/div/div'
    remove_regto_account=By.XPATH,'/html/body/ul/li[2]'
    post_mail=By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/label/span[1]/span'
    remove_save_btn=By.XPATH,'/html/body/div[4]/div/div[3]/div/button[2]'

    # 点击方法
    def click_more_option(self):
        self.click_i(self.more_option)

    def click_remove_regto_account(self):
        self.click_i(self.remove_regto_account)

    def click_post_mail(self):
        self.click_i(self.post_mail)

    def click_remove_save_btn(self):
        self.click_i(self.remove_save_btn)

#  通过账号注册
class Locator_regto_byaccount(BaseAction):
    user = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/ul/div[3]/a/li'
    registmanage = By.XPATH, '/html/body/div/div/div[3]/section/div/div[2]/div[1]/div/div/div/div[3]'
    regto_account = By.XPATH, '//*[@id="pane-registerManager"]/div/div[1]/form/div[4]/button'
    by_account=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[1]/form/div[1]/div/div/label[2]/span[1]/span'
    exist_account=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[1]/form/span'
    search_user=By.XPATH,"/html/body/div[4]/div/div/section/div[1]/div[1]/input"
    choose_user=By.XPATH,'/html/body/div[4]/div/div/section/div[2]/div[1]/div/div[1]/div/label/span[1]/span'
    confirm_btn=By.XPATH,'/html/body/div[4]/div/div/section/div[3]/div[2]/button[2]'
    role = By.XPATH, '/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[1]/form/div[4]/div/div/div[2]/input'
    select_role1 = By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[3]"
    select_role2 = By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[6]"
    next_btn = By.XPATH, '/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div[1]/button[2]'
    regto_account_save_btn = By.XPATH, '/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div[2]/button[3]'
    regto_account_pop_closebtn = By.XPATH, '/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div[3]/button'
#     输入方法
    def enter_keyword_search_user(self,text):
        self.input_things(self.search_user,text)

#     点击方法
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
    user_create_other = By.XPATH, '//*[@id="pane-accountManager"]/div/div[2]/div[1]/div[3]/table/tbody'
    create_acount_page = By.XPATH, '/html/body/div[2]'
    edit_acount_page=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[3]/div/div[1]'
    delete_acount_page=By.XPATH,'/html/body/div[3]/div/div[2]'
    edit_pw_suf_pop=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[4]/div/div[2]/div/div[2]/div'
    account_state = By.XPATH, '/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]'
    invite_user_pop=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div/div/div[2]/p'
    select_role = By.XPATH, "(//li[@class='el-select-dropdown__item'])[4]"
    next_btn=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[3]/div/div[1]/button[2]'
    regto_account_pop=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div'
    edit_regto_account_pop=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[2]/div'
    remove_regto_acount=By.XPATH,'/html/body/div[1]/div/div[3]/section/div/div[2]/div[2]/div[2]/div/div[2]/div[1]'


    # 账号管理验证页面
    def get_accountmanage(self):
        WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located(self.user_create_other))
        return self.driver.find_element(*self.user_create_other).text

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

