class Women:

    def __init__(self,name):

        self.name = name
        self.__age = 18

    def __secret(self):

        print("%s 的年龄是　%d" % (self.name,self.__age))


xiaofang = Women("小芳")
#伪私有方法，在外界不能直接被调用
print(xiaofang._Women__age)

xiaofang._Women__secret()

