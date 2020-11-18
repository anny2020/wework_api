from weixin.api.base_api import BaseApi

class Access(BaseApi):


    #创建成员
    def add_mem(self,userid,name,mobile,token,department=None):
        if department is None:
            department = [1]
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
            "json": {'userid':userid,'name': name,'mobile':mobile,'department':department}
        }
        r = self.send_api(data)
        return r


        #读取成员
    def get_mem(self,userid,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}",
            "params":
                {"userid": userid}
        }
        r = self.send_api(data)
        return r

        #更新成员
    def update_mem(self,userid,name,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
            "json": {'userid': userid,'name': name}
        }
        r = self.send_api(data)
        return r

        #删除成员
    def del_mem(self,userid,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}",
            "params": {'userid': userid}
        }
        r = self.send_api(data)
        return r

        #批量删除成员
    def muldel(self,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token={token}",
            "json": { "useridlist": ["liliu", "lily04"]}
        }
        param = { "useridlist": ["liliu", "lily04"]}
        r = self.send_api(data)
        return r

        #获取部门成员
    def get_depmem(self,department_id,fetch_child,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={token}",
            "params": {'department_id': department_id,'fetch_child': fetch_child}
        }
        r = self.send_api(data)
        return r

        #获取部门成员详情
    def get_depmeminfo(self,department_id,fetch_child,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token={token}",
            "params": {'department_id':department_id,'fetch_child': fetch_child}
        }
        r = self.send_api(data)
        return r

#获取企业活跃成员数
    def get_active_stat(self,date,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get_active_stat?access_token={token}",
            "json": {"date": date}
        }
        r = self.send_api(data)
        return r

