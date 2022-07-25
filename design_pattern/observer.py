# 观察者模式

class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print("Failed to add: {}".format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print("Failed to remove: {}".format(observer))

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = new_value
        except ValueError as e:
            print("Error: {}".format(e))
        else:
            self.notify()


class HexFormatter:
    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__, publisher.name, hex(publisher.data)))


class BinaryFormatter:
    def notify(self, publisher):
        print("{}: '{}' has now binary data = {}".format(type(self).__name__, publisher.name, bin(publisher.data)))


def run1():
    df = DefaultFormatter('test1')
    print(df)

    hf = HexFormatter()

    df.add(hf)
    df.data = 3
    print(df)

    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)

    df.remove(hf)
    df.data = 13
    print(df)
    """
    DefaultFormatter: 'test1' has data = 0

    HexFormatter: 'test1' has now hex data = 0x3
    DefaultFormatter: 'test1' has data = 3

    HexFormatter: 'test1' has now hex data = 0x15
    BinaryFormatter: 'test1' has now binary data = 0b10101
    DefaultFormatter: 'test1' has data = 21

    BinaryFormatter: 'test1' has now binary data = 0b1101
    DefaultFormatter: 'test1' has data = 13

    """

########################################################################################################################

from abc import ABCMeta, abstractmethod


class NewsPublisher:  # subject
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return 'Got News:' + self.__latestNews


class Subscriber(metaclass=ABCMeta):  # Observer

    @abstractmethod
    def update(self):
        pass


class ConcreteSubscriber1(Subscriber):  # ConcreteObserver
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class ConcreteSubscriber2(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


def run2():
    news_publisher = NewsPublisher()
    for Subscribers in [ConcreteSubscriber1, ConcreteSubscriber2]:  # 创建观察者对象
        Subscribers(news_publisher)

    news_publisher.addNews('HELLO WORLD')
    news_publisher.notifySubscribers()
    news_publisher.detach()
    news_publisher.addNews('SECOND NEWS')
    news_publisher.notifySubscribers()
    '''
    ConcreteSubscriber1 Got News:HELLO WORLD
    ConcreteSubscriber2 Got News:HELLO WORLD
    ConcreteSubscriber1 Got News:SECOND NEWS
    '''


########################################################################
class P:      # 发布
    def __init__(self):
        self.__s_list = []
        self.__news = None

    def attach(self, s):
        self.__s_list.append(s)

    def detach(self, s):
        self.__s_list.remove(s)

    def add_news(self, new):
        # 添加新闻
        self.__news = new

    def get_news(self):
        return self.__news

    def notify(self):
        # 通知所有订阅者，即调用订阅者的update方法，并传入数据
        for s in self.__s_list:
            # s.update(self.__news)         # 通知并传数据
            s.update2()                    # 通知，可由订阅者自行处理如调用发布者的get_news方法获取数据


class S1:        # 订阅
    def __init__(self, P):
        self.P = P

    def join_subscribe(self):
        # 调用发布者的添加订阅，将自己加入发布者的订阅者名单中
        self.P.attach(self)

    def update(self, data):
        # 接收订阅消息，交给发布者调用
        print('receive notify, data from Publisher  ', data)

    def update2(self):
        new = self.P.get_news()
        print(new)

    def cancel_subscribe(self):
        # 取消订阅
        self.P.detach(self)

class S2:       # 订阅
    def __init__(self, P):
        self.P = P

    def join_subscribe(self):
        # 调用发布者的添加订阅，将自己加入发布者的订阅者名单中
        self.P.attach(self)

    def update(self, data):
        # 接收订阅消息，交给发布者调用
        print('receive notify, data from Publisher  ', data)

    def update2(self):
        new = self.P.get_news()
        print(new)

    def cancel_subscribe(self):
        # 取消订阅
        self.P.detach(self)



def demo():
    # 创建发布者
    p = P()

    # 创建订阅者(加入发布者的订阅者名单中)
    s1 = S1(p)
    s1.join_subscribe()
    s2 = S2(p)
    s2.join_subscribe()

    #  发布者添加消息
    p.add_news('this is a message')
    # 通知所有订阅者
    p.notify()

    # s1取消订阅
    s1.cancel_subscribe()
    print('s1取消订阅')

    #  发布者添加消息
    p.add_news('this is an another message')
    # 通知所有订阅者，此时s1不再接收
    p.notify()


if __name__ == '__main__':
    # run1()
    # run2()
    demo()



