# unittest单元测试之mock.patch

本篇继续介绍mock里面另一种实现方式，patch装饰器的使用,patch() 作为函数装饰器，为您创建模拟并将其传递到装饰函数.



# patch简介

1.unittest.mock.patch（target，new = DEFAULT，spec = None，create = False，spec_set = None，autospec = None，new_callable = None，** kwargs ）

- target参数必须是一个str,格式为'package.module.ClassName'，
  注意这里的格式一定要写对，如果你的函数或类写在pakege名称为a下，b.py脚本里，有个c的函数（或类），那这个参数就写“a.b.c”
- new参数如果没写，默认指定的是MagicMock
- spec=True或spec_set=True，这会导致patch传递给被模拟为spec / spec_set的对象
- new_callable允许您指定将被调用以创建新对象的不同类或可调用对象。默认情况下MagicMock使用。

# 函数案例讲解

1.接着上一篇[python笔记23-unittest单元测试之mock](https://www.cnblogs.com/yoyoketang/p/9346660.html)，新建一个temple.py,写入以下代码

```python
# 保存为temple.py
 
# coding:utf-8
# 作者：上海-悠悠 QQ交流群：588402570
 
def zhifu():
    '''假设这里是一个支付的功能,未开发完
    支付成功返回：{"result": "success", "reason":"null"}
    支付失败返回：{"result": "fail", "reason":"余额不足"}
    reason返回失败原因
    '''
    pass
 
def zhifu_statues():
    '''根据支付的结果success or fail，判断跳转到对应页面'''
    result = zhifu()
    print(result)
    try:
        if result["result"] == "success":
            return "支付成功"
        elif result["result"] == "fail":
            print("失败原因：%s" % result["reason"])
            return "支付失败"
        else:
            return "未知错误异常"
    except:
        return "Error, 服务端返回异常!"
```



2.用mock.patch实现如下：

```python
# coding:utf-8
from unittest import mock
import unittest
import temple
# 作者：上海-悠悠 QQ交流群：588402570
 
class Test_zhifu_statues(unittest.TestCase):
    '''单元测试用例'''
 
    @mock.patch("temple.zhifu")
    def test_01(self, mock_zhifu):
        '''测试支付成功场景'''
        # 方法一：mock一个支付成功的数据
        # temple.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})
 
        # 方法二：mock.path装饰器模拟返回结果
        mock_zhifu.return_value = {"result": "success", "reason":"null"}
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")
 
    @mock.patch("temple.zhifu")
    def test_02(self, mock_zhifu):
        '''测试支付失败场景'''
        # mock一个支付成功的数据
 
        mock_zhifu.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        self.assertEqual(statues, "支付失败")
 
if __name__ == "__main__":
    unittest.main()
```

# 类和方法案例

1.如果前面的temple.py里面不是函数，是写的类和方法，如何去使用mock?

```python
# 保存为temple.py
 
# coding:utf-8
# 作者：上海-悠悠 QQ交流群：588402570
class Zhifu():
    def zhifu(self):
        '''假设这里是一个支付的功能,未开发完
        支付成功返回：{"result": "success", "reason":"null"}
        支付失败返回：{"result": "fail", "reason":"余额不足"}
        reason返回失败原因
        '''
        pass
 
class Statues():
    def zhifu_statues(self):
        '''根据支付的结果success or fail，判断跳转到对应页面'''
        result = Zhifu().zhifu()
        print(result)
        try:
            if result["result"] == "success":
                return "支付成功"
            elif result["result"] == "fail":
                print("失败原因：%s" % result["reason"])
                return "支付失败"
            else:
                return "未知错误异常"
        except:
            return "Error, 服务端返回异常!"
```

2.用例设计如下

```python
# coding:utf-8
from unittest import mock
import unittest
from temple_class import Zhifu,Statues
# 作者：上海-悠悠 QQ交流群：588402570
 
class Test_zhifu_statues(unittest.TestCase):
    '''单元测试用例'''
 
    @mock.patch("temple_class.Zhifu")
    def test_01(self, mock_Zhifu):
        '''测试支付成功场景'''
        a = mock_Zhifu.return_value  # 先返回实例，对类名称替换
        # 通过实例调用方法，再对方法的返回值替换
        a.zhifu.return_value = {"result": "success", "reason":"null"}
        # 根据支付结果测试页面跳转
        statues = Statues().zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")
 
    @mock.patch("temple_class.Zhifu")
    def test_02(self, mock_Zhifu):
        '''测试支付失败场景'''
        b = mock_Zhifu.return_value  # 先返回实例，对类名称替换
        # 通过实例调用方法，再对方法的返回值替换
        b.zhifu.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = Statues().zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付失败")
 
if __name__ == "__main__":
    unittest.main()
```

3.相当于函数来说，这里主要多一步，要先对类的名称进行mock一次"a = mock_Zhifu.return_value",再通过实例去调用方法



[推荐unit test 之mock 用法_liuskyter的博客-CSDN博客_mock test](https://blog.csdn.net/liuskyter/article/details/103177076)







