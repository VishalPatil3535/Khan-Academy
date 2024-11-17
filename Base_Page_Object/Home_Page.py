from selenium.webdriver.common.by import By


class Home_Page_objects:
    home_page_title = "Khan Academy"
    explore_button_css = "._19zgqrew"
    class_10_chem_xpath = "//span[.='Class 10 Chem']"
    course_title_xpath = "//h1[.='Class 10 Chemistry (India)']"
    course_title = "Class 10 Chemistry (India)"
    level_up_button_linktext = "Level up"
    welcome_text_title = "Identify molecular formulas (practice) | Khan Academy"
    Khan_Academy_refresh_button_css = "._1rt6g9t"
    back_title = "Back Button"

    def __init__(self,driver):
        self.driver = driver


    def click_explore_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.explore_button_css).click()

    def click_class_10_button(self):
        self.driver.find_element(By.XPATH,self.class_10_chem_xpath).click()

    def check_course_title(self):
        self.driver.find_element(By.XPATH, self.course_title_xpath).text()

    def click_level_up_button(self):
        self.driver.find_element(By.LINK_TEXT,self.level_up_button_linktext).click()

    def click_khan_academy_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.Khan_Academy_refresh_button_css).click()
