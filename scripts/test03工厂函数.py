
import pytest
 # 设置工厂函数
# @pytest.fixture(scope="class",autouse=True,params=[1,2,3])

@pytest.fixture(params=[1,2,3,4])

# @pytest.fixture(scope="module")
def before():
    return "hello"

class Test04():
    def test_delete(self):
        print("删除成功")
    def test_get(self,before):
        print("查询成功",before)
    def test_put(self):
        print("修改成功")
    def test_post(self):
        print("新增成功")


# 输出结果
# scripts\test03工厂函数.py 删除成功
# .查询成功 hello
# .查询成功 hello
# .查询成功 hello
# .查询成功 hello
# .修改成功
# .新增成功
# .

