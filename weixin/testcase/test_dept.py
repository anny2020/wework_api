import allure
import pytest

from weixin.api.base_api import BaseApi
from weixin.api.department import DeptApi
from weixin.testcase.data import Data


class TestDept(BaseApi):


    def setup(self):
        self.dept = DeptApi()


        # 集成测试部门相关
    @allure.feature('部门管理')
    @pytest.mark.parametrize("name,name_en,parentid,id,update_name" ,Data().create_data_dept())
    def test_all_department(self,name,name_en,parentid,id,update_name,token):
        try:
            # 创建一个部门，对结果断言
            assert self.dept.add_dept(name,name_en,parentid,id,token)['errmsg'] == "created"
        except AssertionError as e:
            if "department existed" in e.__str__():
                # 如果部门已经存在了，就进行删除操作
                assert self.dept.del_department(id,token)['errmsg'] == 'deleted'
                # 删除后再进行添加部门
                assert self.dept.add_dept(name,name_en,parentid,id,token)['errmsg'] == "created"
                # 查看部门名称是否正确,这里部门可能是有层级的，取值时要取整个列表，再迭代比较
                if len(self.dept.get_deptlist(id,token)['department']) > 0:
                    for i in self.dept.get_deptlist(id,token)['department']:
                        if i['name'] == name:
                            print("创建部门成功")
                else:
                    assert self.dept.get_deptlist(id,token)['department'][0]['name'] == name
        # 更新部门
        assert self.dept.update_department(id,update_name,token)['errmsg'] == "updated"
        # 删除部门
        assert self.dept.del_department(id,token)['errmsg'] == 'deleted'