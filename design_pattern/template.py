# @Author 
# @Date 2024-12-10
# @File: template.go
# @Description: 模板模式（Template Method Pattern）是一种行为型设计模式，它定义了一个操作的框架，并允许子类通过实现部分步骤来实现该操作的细节。
# 也就是说，模板模式通过将固定的算法框架留给父类，而将算法中可变的部分交给子类来实现，从而避免重复代码的同时，保持了灵活性。


class AbstractClass:
    def template_method(self):
        """
        模板方法
        """
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        """
        子类可以重写
        """
        pass

    def step2(self):
        """
        子类可以重写
        """
        pass

    def step3(self):
        """
        子类可以重写
        """
        pass

class ConcreteClass1(AbstractClass):
    def step1(self):
        print("ConcreteClass1 step1")

    def step2(self):
        print("ConcreteClass1 step2")

class ConcreteClass2(AbstractClass):
    def step1(self):
        print("ConcreteClass2 step1")

    def step3(self):
        print("ConcreteClass2 step3")


if __name__ == '__main__':
    # 使用模板方法
    class1 = ConcreteClass1()
    class1.template_method()

    class2 = ConcreteClass2()
    class2.template_method()
