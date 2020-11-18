from weixin.api.base_api import BaseApi


class Wework(BaseApi):
    def get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":
                {'corpid': "wwb30512cbc7b69f64",
                'corpsecret': "gIE-ILmAIFzsuY7JXOrppwYt1rhKSBohBzGF4ad-tBk"}
        }
        r = self.send_api(data)
        try:
            return r['access_token']
        except Exception as e:
            raise ValueError("requests token error")

