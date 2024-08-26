from selenium.webdriver.common.by import By

class credentials:
    username = "email"
    password = "password"

    def enterCredentials(self, driver):
        input_username = driver.find_element(By.ID, "username")
        input_username.send_keys(self.username)

        input_password = driver.find_element(By.ID, "password")
        input_password.send_keys(self.password)