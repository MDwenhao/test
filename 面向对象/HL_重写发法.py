class Animal:
    def eat(self):
        print("吃－－－")
    def drink(self):
        print("喝－－－")
    def run(self):
        print("跑－－－")
    def sleep(self):
        print("睡－－－")

class Dog(Animal):

    def bark(self):
        print("汪汪叫")

class xiangtianquan(Dog):


    def fly(self):
        print("我会飞")
#重写父类里边的ｂａｒｋ方法
    def bark(self):
        print("教的跟神一样")

class Cat(Animal):

    def catch(self):
        print("抓老鼠")
xtq = xiangtianquan()
xtq.fly()
xtq.drink()
# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.bark()

