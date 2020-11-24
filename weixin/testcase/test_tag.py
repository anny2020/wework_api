import allure
import pytest

from weixin.api.tag import TagApi
from weixin.testcase.data import Data


class TestTag(TagApi):

    def setup(self):
        self.tag = TagApi()

    #集成测试标签相关
    @allure.feature('标签管理')
    @pytest.mark.parametrize("tagname,tagid,uptagname",Data().create_data_tag())
    def test_all_tag(self,tagname,tagid,uptagname,token):
        try:
            #创建标签，对结果断言
            assert self.tag.add_tag(tagname,tagid,token)['errmsg'] == "created"
        except AssertionError as e:
            #如果tagid已经存在，就做删除操作
            if "invalid tagid" in e.__str__():
                self.tag.deltag(tagid,token)
                assert self.tag.add_tag(tagname,tagid,token)['errmsg'] == "created"
        #更新标签
        assert self.tag.update_tag(tagid,uptagname,token)['errmsg'] == "updated"
        assert self.tag.get_tagmem(tagid,token)['tagname'] == uptagname
        print(self.tag.get_tagmem(tagid,token)['tagname'])