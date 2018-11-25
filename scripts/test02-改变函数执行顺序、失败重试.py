import pytest


class Test02():
    @pytest.mark.run(order=4)  # 改变函数运行顺序的插件
    def test_delete(self):
        print("删除成功")

    @pytest.mark.run(order=2)
    def test_put(self):
        print("修改成功")
        assert 0  # 断言失败是为了失败重试的插件执行，在配置文件中添加--reruns x （x表示失败重试次数）

    @pytest.mark.run(order=1)
    def test_post(self):
        print("增加成功")

    @pytest.mark.run(order=3)
    def test_get(self):
        print("查询成功")
