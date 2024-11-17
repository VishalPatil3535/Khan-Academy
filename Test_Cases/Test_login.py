import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.Read_property import Read_Config
from Base_Page_Object.Login_Page import Login_page
from utilities.custom_logger import log_maker
from utilities import excel_utilit
from Base_Page_Object.Home_Page import Home_Page_objects



class Test_login_page:
    read_property = Read_Config()
    base_url = read_property.login_url()
    username = read_property.login_username()
    password = read_property.login_password()
    log_details = log_maker.log_gen()
    path = ".\\Test_Data\\TestDataForLogin.xlsx"

    def test_login_01(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        og_title= self.driver.title
        ac_title = "Khan Academy | Free Online Courses, Lessons & Practice"
        if og_title == ac_title:
            assert True
        else:
            assert False
        self.lp = Login_page(self.driver)
        self.lp.click_login_link()
        # self.lp.enter_email(self.username)
        # self.lp.enter_password(self.password)
        self.driver.save_screenshot(".\\Screenshot\\screenshot1.png")
        self.lp.click_login_button()
        self.log_details.info("***************Test_login_01**************")

    def test_login_data_driven_02(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        og_title= self.driver.title
        ac_title = "Khan Academy | Free Online Courses, Lessons & Practice"
        if og_title == ac_title:
            assert True
        else:
            assert False
        self.lp = Login_page(self.driver)
        self.lp.click_login_link()
        self.username = excel_utilit.read_data(self.path,"Sheet1",2,1)
        self.password = excel_utilit.read_data(self.path,"Sheet1",2,2)
        self.lp.enter_email(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()
        self.driver.save_screenshot(".\\Screenshot\\screenshot1.png")
        self.log_details.info("***************Test_login_01**************")


    def test_home_page_03(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.base_url)
        self.lp = Login_page(self.driver)
        og_title= self.driver.title
        ac_title = self.lp.title1
        if og_title == ac_title:
            assert True
        else:
            assert False
        self.lp.click_login_link()
        self.username = excel_utilit.read_data(self.path,"Sheet1",2,1)
        self.password = excel_utilit.read_data(self.path,"Sheet1",2,2)
        self.lp.enter_email(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login_button()
        self.home = Home_Page_objects(self.driver)
        home_title = self.driver.title
        print(home_title)
        act_title = self.home.home_page_title
        print(act_title)
        if home_title == act_title:
            assert True
        else:
            assert False
        self.home.click_explore_button()
        self.home.click_class_10_button()
        time.sleep(5)
        og = self.driver.find_element(By.XPATH,self.home.course_title_xpath).text
        print(og)
        # act = self.home.course_title
        # print(act)    # if og == act:
        #     assert True
        # else:
        #     assert False
        # time.sleep(5)
        # self.home.click_level_up_button()
        # ti = self.driver.title
        # act1 = self.home.welcome_text_title
        # if ti == act1:
        #     assert True
        # else:
        #     assert False
        # self.home.click_khan_academy_button()
        # title = self.driver.title
        # back = self.home.back_title
        # if title == back:
        #     assert True
        # else:
        #     assert False




