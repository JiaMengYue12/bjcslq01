class  Test01():
    # 默认情况下，类名、方法名必须以test开头
    # 类级别是在执行所有测试用例之前、之后执行一次
    def setup_class(self):
        print("请先登录")

    def teardown_class(self):
        print("用例执行完毕")

    # setup/teardown是在每一条测试用例的前后都会执行
    def setup(self):
        print("登录成功")

    def teardown(self):
        print("执行下一条用例")

    def test01(self):
        print("test01执行了")

    def test02(self):
        print("test02执行了")

