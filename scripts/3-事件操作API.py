import time
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'


driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#存储367,2319   更多377,652   使用uiautomatorviewer工具获取到的坐标
# duration是毫秒时间
# driver.swipe(367,2319,377,652,duration=3000)

# 使用location定位坐标
cun=driver.find_element_by_xpath("//*[contains(@text,'存储')]")
geng=driver.find_element_by_xpath("//*[contains(@text,'更多')]")
# 从存储滑动到更多  swipe
# driver.swipe(cun.location.get("x"),cun.location.get("y"),geng.location.get("x"),geng.location.get("y"),duration=3000)

# 从存储滚动到更多  scroll
# driver.scroll(cun,geng)

# 把存储拖拽到更多  drag_and_drop  把存储拖到更多的位置
# driver.drag_and_drop(cun,geng)

# 把设置界面启动后，置于后台十秒  background_app   热启动
driver.background_app(10)

time.sleep(3)
driver.quit()