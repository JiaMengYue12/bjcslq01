import time
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'


driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 获取手机当前时间
print(driver.device_time)

# 获取手机的宽高
print(driver.get_window_size())

# 发送键码到手机
# time.sleep(1)
# driver.keyevent(25)
# time.sleep(1)
# driver.keyevent(24)

# 打开通知栏  测试：1)通知栏功能是否可以打开2）点击通知栏的消息是否可以跳转
# driver.open_notifications()

# 获取手机当前连接网络
# print(driver.network_connection)

# 设置当前网络类型
# driver.set_network_connection(6)
# print(driver.network_connection)

# 截图
driver.get_screenshot_as_file("../jietu/%s.png" % time.strftime("%y-%m-%d_%H-%M-%S"))

time.sleep(3)
driver.quit()