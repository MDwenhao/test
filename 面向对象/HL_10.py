# date1 = {"鲤鱼":[10,10.5],"金鱼":[8,6.5], "黑鱼":[7,4.7]}
# date2 = {"草鱼":[2,2.7], "无语": [3, 12]}
# date = {"2019年9月21日":date1, "2019年10月23日": date2}
# nums = 0
# numsmany = 0
# day = ""
# dates = {}
# for day,dates in date:
#     print("%s 钓鱼的记录" % day)
#     for name,list in dates:
#
#         nums += list[0]
#         numsmany += list[0]*list[1]
#         print("%s")
date1 = {'鲤鱼': [10, 10.5], '金鱼': [8, 6.2], '酥鱼': [9, 12.5]}
date2 = {'鲤鱼': [10, 10.5], '金鱼': [8, 6.2], '酥鱼': [9, 12.5]}
date3 = {'鲤鱼': [10, 10.5], '金鱼': [8, 6.2], '酥鱼': [9, 12.5]}
zj = {'10月1日': date1, '10月2日': date2,
              '10月3日': date3}
sl=0
zje=0
k={}
for day,dayy in zj.items():
    for zl,zll in dayy.items():
        if zll[0] % 2 ==0:
            sl+=zll[0]
            zje+=zll[0]*zll[1]
            print("%s为偶数的鱼:%s,数量%d,单价%.2f"%(day,zl,zll[0],zll[1]))
            print("为偶数鱼的总数量为:%d,总金额为%.2f"%(sl,zje))