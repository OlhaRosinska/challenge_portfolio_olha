 from pages.base_page import BasePage


 class LoginPage(BasePage):
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//[@id='password']"
     sign_in_button_xpath = "//[text()='Sign in']"
     remind_password_field_xpath = "//[text()='Remind password']"
     English_field_xpath = "//[text()='English']"
     Polski_field_xpath = "//[text()='Polski']"
     Scouts_Panel_field_xpath = "//[contains(text(),'Scouts Panel')]"

    def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)
