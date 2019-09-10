class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod
    def sho_tool_count(cls):

        print("工具对象的数量　%d" % cls.count)

    def __init__(self,name):

        self.name = name

        Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("榔头")
#一类名点的方式
Tool.sho_tool_count()