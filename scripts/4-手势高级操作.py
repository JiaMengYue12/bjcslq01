import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'


driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)

# 一 轻敲 tap
# 基于元素  导包TouchAction 通过perform执行  也可以基于坐标
# wlan=driver.find_element_by_xpath("//*[@text='WLAN']")
# TouchAction(driver).tap(wlan).perform()


# 二 手指按操作  press
# 业务场景:
#       1.进入设置
#       2.点击WLAN选项

# wlan=driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# TouchAction(driver).press(wlan).release().perform()

# 三 长按


# 四 move_to
"""
    需求：
        1.进入设置
        2. 向上滑动屏幕到可见"安全"选项
        3.进入到安全
        4.点击屏幕锁定方式
        5.点击图案
        6.绘制图案
"""

# wlan=driver.find_element_by_xpath("//*[@text='WLAN']")
#
# cunchu=driver.find_element_by_xpath("//*[@text='存储']")
#
# driver.drag_and_drop(cunchu,wlan)
#
# driver.find_element_by_xpath("//*[@text='安全']").click()
#
# driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定方式')]").click()
#
# driver.find_element_by_xpath("//*[@text='图案']").click()
#
# time.sleep(3)
# 240,848  720,1329    1206,1814
# TouchAction(driver).press(x=240,y=848).wait(100).move_to(x=720-240,y=1329-848).wait(100).\
#     move_to(x=1206-720,y=1814-1329).wait(100).release().perform()

# TouchAction(driver).press(x=240,y=848).wait(100).move_to(x=706-240,y=0).wait(100).release().perform()

time.sleep(3)
driver.quit()