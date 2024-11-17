
from selenium.webdriver.common.by import By


class Login_page:
    login_link_linktext = "Log in"
    email_text_field_xpath = "//*[@id='username-field']"
    password_text_field_css = "#current-password-field"
    login_button_xpath = "//button[@type='submit']"
    title1 = "Khan Academy | Free Online Courses, Lessons & Practice"

    def __init__(self,driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(By.LINK_TEXT,self.login_link_linktext).click()

    def enter_email(self,username):
        self.driver.find_element(By.XPATH,self.email_text_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_text_field_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.CSS_SELECTOR,self.password_text_field_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.password_text_field_css).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()