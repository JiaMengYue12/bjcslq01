"""
    目标：pytest高级用法二
        1. 跳过函数使用
            @pytest.mark.skipif(条件,原因)
        2. 标记预期失败
            @pytest.mark.xfail(条件，原因)
        3. 参数化

"""
import pytest


class Test04():
    def test_post(self):
        print("新增失败")
        return False

    @pytest.mark.skipif(test_post=False, reason="条件成立，此方法被跳过！")
    def test_delete(self):
        print("删除成功")

    # @pytest.mark.xfail(1>0,reason="条件成立，标记预期失败！")
    # @pytest.mark.xfail(test_post=False,reason="条件成立，标记预期失败！")
    def test_get(self):
        print("查询成功")

    def test_put(self):
        print("修改成功")