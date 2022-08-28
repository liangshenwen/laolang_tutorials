import threading
import time
# 这里使用方法__new__来实现单例模式
class Singleton(object):  # 抽象单例
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            # Singleton的父类为object类
            obj_clazz = super(Singleton, cls)
            cls._instance = obj_clazz.__new__(cls)
            # 因为object.__new__() 只接受cls一个参数, 因此这里如果这样子写，如果子类中构造函数有入参，将会抛异常：
            # TypeError: object.__new__() takes exactly one argument (the type to instantiate)
            # cls._instance = obj_clazz.__new__(cls, *args, **kw)
        return cls._instance

# 总线
class Bus(Singleton):
    def __init__(self, version):
        self.version = version
        super().__init__()

    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("Bus"+self.version + " is sending Signal Data...", data)
        self.lock.release()

# 线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus("1.0")
        self.my_bus.sendData(self.name)


if __name__ == "__main__":
    for i in range(3):
        print("Entity %d begin to run..." % i)
        my_entity = VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()