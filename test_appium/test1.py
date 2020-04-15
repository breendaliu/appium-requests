from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        # 平台
        caps["platformName"] = "android"
        # 设备名字
        caps["deviceName"] = "test01"
        caps["automationName"] = "uiautomator2"
        # 包名
        caps["appPackage"] = "com.xueqiu.android"
        # 入口
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 清理数据，为True时不清理
        caps["noReset"] = True
        # 提速参数，如果app在，不杀，继续运行
        caps["dontStopAppOnReset"] = True
        # 是否输入非英文语言，true为是
        caps["unicodeKeyBoard"] = True
        # 是否恢复语言设置
        caps["resetKeyBoard"] = True
        # 跳过系统安装
        caps["skipServerInstallation"] = True
        # 方法一，指定Chromedriver所在文件夹，从中获取可用版本,不可用则使用方法二
        # caps["chromedriverExecutableDir"] = "E:/Chromedriver"
        # 方法二，强行指定Chromedriver版本
        caps["chromedriverExecutable"] = "E:\Chromedriver\chromedriver_2.20.exe"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_webview_gmkh(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        WebDriverWait(self.driver, 60).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_xueying_SJY").click()
        # for i in range(5):
        #     print(self.driver.window_handles)
        WebDriverWait(self.driver, 60).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        number = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(number))
        self.driver.find_element(*number).send_keys("18534163095")
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入验证码"]').send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, ".open_form-submit_1Ms").click()
        toast = (self.driver.find_element(By.CSS_SELECTOR, ".Toast_toast_22U div span")).text
        assert "请输入正确的验证码！" in toast
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(MobileBy.ID, "action_bar_close").click()


