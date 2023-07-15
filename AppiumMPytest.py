from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as Remote
import requests
import pytest
from time import sleep

class Test_FreeveeMAutomation():
    @pytest.fixture
    def Web_data_booting(self):
        Device_Cap = {
            "platformName": "Android",
            "appium:platformVersion": "11",
            "appium:deviceName": "GalaxyM21",
            "appium:udid": "RZ8R120KBZV"
            }
        self.idriver = webdriver.Remote("http://localhost:4723/wd/hub", Device_Cap)
        self.idriver.swipe(start_x=530, start_y= 2024, end_x=530, end_y=900)
        self.idriver.find_element(by=By.XPATH, value= '//android.view.ViewGroup[@content-desc="0"]').click()
        self.idriver.find_element(by=By.XPATH, value= '//android.view.ViewGroup[@content-desc="0"]').click()
        self.idriver.find_element(by=By.XPATH, value= '//android.view.ViewGroup[@content-desc="0"]').click()
        self.idriver.find_element(by=By.XPATH, value= '//android.view.ViewGroup[@content-desc="0"]').click()

        sleep(5)
        Desired_Cap = {
            "platformName": "Android",
            "appium:platformVersion": "11",
            "appium:deviceName": "GalaxyM21",
            "appium:automationName": "Appium",
            "appium:appPackage": "com.amazon.imdb.tv.mobile.app",
            "appium:appActivity": "com.amazon.imdb.tv.mobile.app.rn.PlatformReactNativeActivity"
            }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", Desired_Cap)
        sleep(10)
        yield

    def test_M_TC1(self, Web_data_booting):
        searchTab = self.driver.find_element(by=By.XPATH, value= '//android.view.ViewGroup[@content-desc="Search Freevee"]/android.view.ViewGroup').click()
        sleep(2)
        searchTextBox = self.driver.find_element(by=By.XPATH, value= '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText').send_keys('Alex Rider')
        sleep(2)
        SearchResult1Select = self.driver.find_element(by=By.XPATH, value= '//android.widget.Button[@content-desc="Title. Alex Rider: Operation Stormbreaker.  Watch Now"]/android.widget.TextView').click()
        sleep(15)

        self.driver.press_keycode(85) # Play/Pause
        sleep(10)

        self.driver.back()
        self.driver.back()
        self.driver.back()
        self.driver.back()

        print("M_TC1 Passed")