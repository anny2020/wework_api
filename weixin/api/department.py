from weixin.api.base_api import BaseApi


class DeptApi(BaseApi):

     # 创建部门
    def add_dept(self,name,name_en,parentid,id,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}",
            "json": {
                    "name": name,
                    "name_en": name_en,
                    "parentid": parentid,
                    # "order": order,
                    "id": id
                    }
        }
        r = self.send_api(data)
        return r

    #更新部门
    def update_department(self,id,name,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}",
            "json":
                    {
                    "id": id,
                    "name": name
            }
        }
        r = self.send_api(data)
        return r

    #删除部门
    def del_department(self,id,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}",
            "params": {'id':id}
        }
        r = self.send_api(data)
        return r


    #获取部门列表
    def get_deptlist(self,id,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}",
            "params": {'id': id}
        }
        r = self.send_api(data)
        return r

