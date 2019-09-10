class classdef :
	count = 0
	@classmesthod
	def clsdef(cls):
		print("工具对象的数量是 %d" %cls.count)

    def __init__(self, name):
    	self.name = name

        classmesthod.count += 1

tool1 = classdef("斧头")
tool2 = classdef("榔头")
classdef.clsdef()
