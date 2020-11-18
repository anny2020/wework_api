import requests


class BaseApi:
    def send_api(self,req:dict):
        #请求封装
        return requests.request(**req).json()
