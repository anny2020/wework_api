class Data:

# 生成集成测试人员测试数据
    def create_data_mem(self):
        data = [("wu1weeeeyx" + str(x), "zhangsan1", "zhangjiu1", "139%08d" % x) for x in range(10)]
        return data

    def create_data_dept(self):
        data = [("naae123" +str(x),"yf12a"+str(x),1,30+x,"upndd23"+str(x)) for x in range(2)]
        return data

    def create_data_tag(self):
        data = [("tag123"+str(x),30+x,"uptag345"+str(x)) for x in range(2)]
        return data