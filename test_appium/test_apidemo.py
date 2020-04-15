from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestApidemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test02"
        caps["automationName"] = "uiautomator2"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_view(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Views").click()
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # toast定位使用(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        toast=self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "Clicked" in toast
        assert "Search" in toast

    def teardown(self):
        sleep(5)
        self.driver.quit()