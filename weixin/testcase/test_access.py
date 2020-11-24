from typing import re

import allure
import pytest
from weixin.api.access import Access
from weixin.testcase.data import Data


@allure.feature('人员管理')
class Test_Access:

    def setup(self):
        self.access = Access()

    # 集成测试人员相关
    TEST_CASE_LINK="https://www.tapd.cn/59667731/bugtrace/bugs/view?bug_id=1159667731001004077&url_cache_key=6a0263891bd3ab6d01f9788b14dfafd3"
    @allure.testcase(TEST_CASE_LINK,'测试用例标题')
    @allure.story(" 创建人员、更新人员、删除人员")
    @pytest.mark.parametrize("userid,name,upname,mobile" ,Data().create_data_mem())
    def test_all_member(self,userid,name,mobile,upname,token):
        try:
            # 创建一个成员，对结果断言
            with allure.step("step1:添加人员"):
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
        with allure.step("step2:更新人员"):
            assert self.access.update_mem(userid,upname,token)['errmsg'] == "updated"
        assert self.access.get_mem(userid,token)['name'] == upname
        # 删除
        with allure.step("step3:删除人员"):
            assert self.access.del_mem(userid,token)['errmsg'] == 'deleted'
        assert self.access.get_mem(userid,token)['errcode'] == 60111

