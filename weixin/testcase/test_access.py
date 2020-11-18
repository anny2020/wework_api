from typing import re

import pytest
from weixin.api.access import Access
from weixin.testcase.data import Data


class Test_Access:

    def setup(self):
        self.access = Access()

    # 集成测试人员相关
    @pytest.mark.parametrize("userid,name,upname,mobile" ,Data().create_data_mem())
    def test_all_member(self,userid,name,mobile,upname,token):
        try:
            # 创建一个成员，对结果断言
            assert self.access.add_mem(userid,name,mobile,token)['errmsg'] == "created"
        except AssertionError as e:
            print(e.__str__())
            if "userid existed" in e.__str__():
                self.access.del_mem(userid,token)
            if "mobile existed" in e.__str__():
                del_userid = re.findall(":(.*)' " ,e.__str__())
                print(del_userid[0])
                self.access.del_mem(del_userid[0])
            assert self.access.add_mem(userid,name,mobile,token)['errmsg'] == "created"
        assert self.access.get_mem(userid,token)['name'] == name
        # 更新一个成员
        assert self.access.update_mem(userid,upname,token)['errmsg'] == "updated"
        assert self.access.get_mem(userid,token)['name'] == upname
        # 删除
        assert self.access.del_mem(userid,token)['errmsg'] == 'deleted'
        assert self.access.get_mem(userid,token)['errcode'] == 60111