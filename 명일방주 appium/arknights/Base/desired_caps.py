from appium.webdriver.webdriver import WebDriver
from appium.options.android import UiAutomator2Options
import os

def get_driver():
    os.environ["ANDROID_HOME"] = r"C:\Users\user\AppData\Local\Android\Sdk"

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "9"
    options.device_name = "emulator-5554"
    options.app_package = "com.YoStarKR.Arknights"
    options.app_activity = "com.u8.sdk.U8UnityContext"
    options.no_reset = True

    driver = WebDriver(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    return driver
