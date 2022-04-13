"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class A(object):

    def foo(self):
        print('foo of A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo fo C')


class D(B, C):
    pass


class E(D):

    def foo(self):
        print('foo in E')
        super().foo()



if __name__ == '__main__':
    d = D()
    d.foo()
    e = E()
    e.foo()
    ##Python中针对类提供了一个内置属性__mro__可以查看方法的搜索顺序
    print(E.__mro__)
