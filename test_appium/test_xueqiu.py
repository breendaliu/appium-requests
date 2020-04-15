# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

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

    def test_search(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
        # 提速方法，模拟器停留在首页，隐藏用例中的点击同意的步骤
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # el2.click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # el3.send_keys("alibaba")
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_search_and_get_price(self):
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        assert float(self.driver.find_element(MobileBy.ID, "current_price").text) > 200

    def test_search_and_get_price_from_hk(self):
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='股票']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@resource-id, "title_container")]//*[@text="股票"]').click()
        # assert float(self.driver.find_element(MobileBy.XPATH, "//*[@text='09988']").text) > 200
        price = (MobileBy.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id, "current_price")]')
        # *price中的*是元组的意思
        assert float(self.driver.find_element(*price).text) > 200
        # 获取元素属性
        print(self.driver.find_element(*price).get_attribute("resourceID"))

    def test_search_chooles(self):
        # 搜索股票，添加到自选，返回后再次搜索，断言已添加
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@resource-id, "title_container")]//*[@text="股票"]').click()
        price1 = (MobileBy.XPATH, '//*[@text="BABA"]/../../..//*[contains(@resource-id, "follow_btn")]')
        self.driver.find_element(*price1).click()
        self.driver.find_element(MobileBy.ID, "action_delete_text").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@resource-id, "title_container")]//*[@text="股票"]').click()
        assert '已添加' == self.driver.find_element(MobileBy.XPATH,
                                                 '//*[@text="BABA"]/../../..//*[contains(@resource-id, "followed_btn")]').get_attribute(
            "text")

    def test_scroll(self):
        size = self.driver.get_window_size()
        # 长按屏幕坐标为x,y的位置， 移动到屏幕的坐标为0.5与0.2的位置，释放，执行
        # 循环10次
        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2) \
                .release() \
                .perform()

    # 上下滑动页面，定位到“4小时前”后进行点击操作
    def test_toast(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("4小时前").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

    # 获取页面元素
    def test_source(self):
        print(self.driver.page_source)

    # 原生页面进行webview测试
    def test_s(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "A股开户").click()
        self.driver.find_element(MobileBy.ID, "phone-number").click()
        self.driver.find_element(MobileBy.ID, "phone-number").send_keys("18534163095")

    def test_webview_context(self):
        # print大部分用于首次测试分析上下文
        # 切入到webview
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        # 打印上下文
        #     for i in range(5):
        #         print(self.driver.contexts)
        #         sleep(0.5)
        #     print(self.driver.page_source)
        # 显示等待：等待上下文数据大于1时，切入webview内部
        WebDriverWait(self.driver, 60).until(lambda x: len(self.driver.contexts) > 1)
        # 切入webview内部
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.page_source)
        # 打印A股开户窗口
        #    print(self.driver.window_handles)
        # 点击A股开户
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI").click()
        # # 打印进入A股开户页面后的窗口
        #     for i in range(5):
        #         print(self.driver.window_handles)
        #         sleep(0.5)
        # 显示等待：等待窗口大于3时，切入列表中最后一个窗口
        WebDriverWait(self.driver, 60).until(lambda y: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.ID, "phone-number")
        # 显示等待：等待phone元素可见时，进行输入操作
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys("18534163095")

    def test_webview_gmkh(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()
        WebDriverWait(self.driver, 60).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_xueying_SJY").click()
        # for i in range(5):
        #     print(self.driver.window_handles)
        WebDriverWait(self.driver, 60).until(lambda  x: len(self.driver.window_handles)> 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        number=(By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(number))
        self.driver.find_element(*number).send_keys("18534163095")
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入验证码"]').send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, ".open_form-submit_1Ms").click()
        toast = (self.driver.find_element(By.CSS_SELECTOR, ".Toast_toast_22U div span")).text
        assert "请输入正确的验证码！" in toast
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(MobileBy.ID, "action_bar_close").click()



    def teardown(self):
        pass
        # sleep(5)
        # self.driver.quit()

    # 提速方法，隐藏退出操作
