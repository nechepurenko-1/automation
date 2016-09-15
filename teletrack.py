# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class teletrack(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_teletrack(self):
        success = True
        wd = self.wd
        wd.get("http://teletrack.ua/login.html")
        wd.find_element_by_css_selector("html.ng-scope").click()
        wd.find_element_by_xpath("//div[@class='panel-content']/div[1]/input").click()
        wd.find_element_by_xpath("//div[@class='panel-content']/div[1]/input").clear()
        wd.find_element_by_xpath("//div[@class='panel-content']/div[1]/input").send_keys("vnechepurenko")
        wd.find_element_by_xpath("//div[@class='panel-content']/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='panel-content']/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='panel-content']/div[2]/input").send_keys("vnechepurenko2015")
        wd.find_element_by_name("btn_login").click()
        wd.find_element_by_xpath("//div[@id='drag_zone']/div/div[1]/div/div[3]/div[3]/div[1]").click()
        wd.find_element_by_xpath("//div[@id='drag_zone']/div/div[1]/div/div[3]/div[3]/div[2]/ul/li[3]/i[1]").click()
        wd.find_element_by_xpath("//a[@id='track_module']/div[1]/img").click()
        wd.find_element_by_css_selector("p").click()
        wd.find_element_by_link_text("GEOZONES").click()
        wd.find_element_by_css_selector("p").click()
        wd.find_element_by_xpath("//a[@id='report_module']/div[1]/img").click()
        wd.find_element_by_xpath("//a[@id='setting_module']/div[1]/img").click()
        wd.find_element_by_xpath("//a[@id='notifications_module']/div[1]/img").click()
        wd.find_element_by_link_text("User").click()
        wd.find_element_by_css_selector("span.icon-enter").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':


    unittest.main()
