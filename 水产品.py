import random
fish_list = [{"date": "2019-9-21", "fishtype": "鲤鱼", "count": 13, "many": 456}]
fish_name = ["鲤鱼", "草鱼", "鲶鱼", "带鱼"]
while True:
    print("请选择操作编号:"
          "1,钓鱼,"
          "2,买鱼"
          "3,查询账单")
    opion = input()
    if opion == "1":
        fish = fish_name[int(random.uniform(0,len(fish_name)))]
        print("你钓到的鱼是 %s" %fish)
        if fish == "鲤鱼":
            fish_list["count"] += 1
            fish_list["many"] += 30
    if opion == "2":
         print("请选择所要买的鱼:"
               "1,鲤鱼"
               "2,草鱼"
               "3,鲶鱼"
               "4,带鱼")
    if opion == "3":
        print("\t时间\t\t水产品\t\t产品数量\t\t收获金额")
        print("%s\t%s\t\t\t%s\t\t\t%s"%(fish_list["date"],
                fish_list["fishtype"],
                fish_list["count"],
                fish_list["many"]))
            