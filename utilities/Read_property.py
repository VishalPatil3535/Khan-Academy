import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\vishalp.AD-DATATEMPLATE\\PycharmProjects\\PythonTask\\Configuration\\conf.ini")

class Read_Config:
    @staticmethod
    def login_url():
        url = config.get("login_in_page","base_url")
        return url

    @staticmethod
    def login_username():
        username = config.get("login_in_page","username")
        return username

    @staticmethod
    def login_password():
        password = config.get("login_in_page", "password")
        return password


