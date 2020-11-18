from weixin.api.base_api import BaseApi


class TagApi(BaseApi):
    # 创建标签
    def add_tag(self,tagname,tagid,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",
            "json": {'tagname': tagname, 'tagid': tagid}
        }
        r = self.send_api(data)
        return r

    # 更新标签名字
    def update_tag(self,tagid,tagname,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",
            "json": {"tagid": tagid, "tagname": tagname}
        }
        r = self.send_api(data)
        return r


    # 删除标签
    def deltag(self,id,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}",
            "params": {"tagid": id}
        }
        r = self.send_api(data)
        return r


    # 获取标签成员
    def get_tagmem(self,tagid,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={token}",
            "params": {"tagid": tagid}
        }
        r = self.send_api(data)
        return r


    # 增加标签成员
    def add_tagmem(self,tagid,userlist,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={token}",
            "json": {"tagid": tagid, "userlist": userlist}
        }
        r = self.send_api(data)
        return r


    # 删除标签成员
    def del_tagname(self,token):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={token}",
            "json": {"tagid": 1, "userlist": ["lily05"], "partylist": 1}
        }
        r = self.send_api(data)
        return r


    ##获取标签列表
    def get_taglist(self,token):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"
        }
        r = self.send_api(data)
        return r

