# 导包
import time
from appium import webdriver

# desired_caps为字典格式 - 常用参数：
desired_caps = {}
# 必填-且正确
desired_caps['platformName'] = 'Android'
# 必填-且正确
desired_caps['platformVersion'] = '5.1'
# 必填，设备名称，通过adb命令（adb devices）获取
desired_caps['deviceName'] = 'emulator-5554'
# APP包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'

# 地址通过Ctrl+p可以获取
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


time.sleep(3)

#获取爱客App的包名和启动名com.vcooline.aike/.umanager.LoginActivity
driver.start_activity("com.vcooline.aike",".umanager.LoginActivity")

driver.quit()