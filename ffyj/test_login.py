import requests
from hamcrest import assert_that, has_string, contains_string
from jsonpath import jsonpath


class TestFfyj:
    def setup_class(self):
        self.host = 'http://192.168.30.185'
        self.port = '8082'

    #登录页面
    def test_login_page(self):
        url = self.host+':'+self.port+'/ffyj/login.html'
        print(url)
        r = requests.get(url)
        # print(r.text)
        # print(r.json())
        print(r.cookies)
        # assert r.status_code == 200


    #用户登录e
    def test_login(self):
        url = self.host+':'+self.port+'/ffyj/admin/login'
        param = {
            'username': '00000',
            'password': '000000'
        }
        r = requests.post(url,data=param)
        # print(r.json())
        # print(r.cookies)
        # assert_that(r.json()['message'],has_string('success'))
        return r.cookies

    #首页
    def test_main(self):
        url = self.host+":"+self.port+'/ffyj/_admin.html'
        cookies = self.test_login()
        r = requests.get(url,params = cookies)
        assert_that(r.text,contains_string('修改密码'))

    #菜单列表
    def test_sfgl(self):
        url = self.host+":"+self.port+"/ffyj/admin/menuList"
        cookies = self.test_login()
        r = requests.get(url,params=cookies)
        # print(r.json())
        # print(r.json()['message'])
        # assert_that(r.json()['message'],contains_string('success'))
        print(jsonpath(r.json(),'$..data..menuName'))
        print(r.json())
        # assert jsonpath.jsonpath(r.json(),'$..name')

    #涉访管理
    def test_sfgl1(self):
        url = self.host+":"+self.port+"/ffyj/page/ffwk/ffgz/gzdx/gzdxList.html"
        cookies = self.test_login()
        r = requests.get(url,params=cookies)
        assert_that(r.text,contains_string('申请列管'))

    #tjxx
    def test_tjxx(self):
        url = self.host+":"+self.port+"/ffyj/admin/api/index/tjxx"
        cookies = self.test_login()
        payload = {'swrylx': 0,
                 'cookies': cookies}
        r = requests.post(url,json=payload)
        print(r.text)


    #gzdx
    def test_gzdx(self):
        url = self.host+":"+self.port+"/ffyj/admin/api/ffwk/ffgz/gzdx/gzdxList"
        cookies = self.test_login()
        headers = {'Cookie': cookies,'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        payload = {'swrylx': '0','sylx': '0'}
        r = requests.post(url,headers=headers,data=payload)
        # print(r.headers)
        print(r.request)

